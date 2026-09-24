#!/usr/bin/env python3
"""Fail-closed release audit for the research artifact and optional paper tree."""
from __future__ import annotations
import argparse, ast, csv, hashlib, json, os, re, subprocess, sys, zipfile
from pathlib import Path
from typing import Any

class DuplicateKey(ValueError): pass

def strict_pairs(pairs):
    d={}
    for k,v in pairs:
        if k in d: raise DuplicateKey(f'duplicate JSON key: {k!r}')
        d[k]=v
    return d

def parse_constant(x): raise ValueError(f'non-finite JSON number: {x}')

def check_json(path:Path):
    json.loads(path.read_text(encoding='utf-8'),object_pairs_hook=strict_pairs,parse_constant=parse_constant)

def sha256(path:Path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()

def safe_rel(root:Path,p:Path):
    rel=p.relative_to(root)
    if rel.is_absolute() or '..' in rel.parts: raise ValueError(f'unsafe path: {rel}')
    return rel.as_posix()

def run(cmd,cwd=None):
    return subprocess.run(cmd,cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

def parse_bib(path:Path):
    s=path.read_text(encoding='utf-8',errors='strict')
    starts=list(re.finditer(r'@\w+\s*\{\s*([^,\s]+)\s*,',s,re.I))
    entries=[]
    for i,m in enumerate(starts):
        block=s[m.start():(starts[i+1].start() if i+1<len(starts) else len(s))]
        def field(name):
            mm=re.search(rf'\b{name}\s*=\s*[{{\"](.*?)[}}\"]\s*,?\s*(?=\n\s*\w+\s*=|\n\s*}})',block,re.I|re.S)
            return re.sub(r'\s+',' ',mm.group(1)).strip() if mm else ''
        entries.append({'key':m.group(1),'title':field('title'),'doi':field('doi'),'url':field('url')})
    return entries

def norm_title(s): return re.sub(r'[^a-z0-9]+','',re.sub(r'[{}\\]','',s).lower())
def norm_doi(s):
    s=s.strip().lower(); s=re.sub(r'^https?://(dx\.)?doi\.org/','',s); return s

def paper_audit(paper:Path):
    out={'present':paper.exists(),'issues':[]}
    if not paper.exists(): return out
    texs=list(paper.rglob('*.tex')); bibs=list(paper.rglob('*.bib'))
    if not texs: out['issues'].append('no TeX source')
    if not bibs: out['issues'].append('no BibTeX source'); return out
    alltex='\n'.join(p.read_text(encoding='utf-8',errors='replace') for p in texs)
    cites=set()
    for m in re.finditer(r'\\cite\w*\s*(?:\[[^]]*\]\s*)*\{([^}]+)\}',alltex):
        cites.update(k.strip() for k in m.group(1).split(',') if k.strip())
    entries=[]
    for b in bibs: entries.extend(parse_bib(b))
    keys=[e['key'] for e in entries]; keyset=set(keys)
    if len(keys)!=len(keyset): out['issues'].append('duplicate bibliography keys')
    missing=sorted(cites-keyset); uncited=sorted(keyset-cites)
    if missing: out['issues'].append(f'missing citation keys: {missing}')
    if uncited: out['issues'].append(f'uncited bibliography entries: {uncited}')
    dois={}; titles={}
    for e in entries:
        if e['doi']:
            d=norm_doi(e['doi'])
            if not re.fullmatch(r'10\.\d{4,9}/\S+',d): out['issues'].append(f"malformed DOI {e['key']}: {e['doi']}")
            dois.setdefault(d,[]).append(e['key'])
        t=norm_title(e['title'])
        if t: titles.setdefault(t,[]).append(e['key'])
    for d,ks in dois.items():
        if len(ks)>1: out['issues'].append(f'duplicate DOI {d}: {ks}')
    for t,ks in titles.items():
        if len(ks)>1: out['issues'].append(f'duplicate normalized title: {ks}')
    out.update({'tex_files':len(texs),'bib_files':len(bibs),'bibliography_entries':len(entries),
                'cited_keys':len(cites),'missing_keys':missing,'uncited_keys':uncited})
    # Claim-language guardrails.
    required=[
      ('caller-supplied',r'caller[- ]supplied'),
      ('not legal ownership',r'(not|neither).{0,40}legal ownership'),
      ('closed world',r'closed[- ]world'),
      ('Android non-claim',r'(not|does not).{0,100}(Android|D8|R8|resource merging)'),
      ('census not random sample',r'(census|complete sampling frame).{0,100}(not.{0,20}(random|representative)|descriptive)'),
    ]
    low=alltex.lower()
    for label,pat in required:
        if not re.search(pat,alltex,re.I|re.S): out['issues'].append(f'missing scope guardrail: {label}')
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--artifact',type=Path,default=Path(__file__).resolve().parents[1])
    ap.add_argument('--paper',type=Path)
    ap.add_argument('--output-json',type=Path)
    ap.add_argument('--output-md',type=Path)
    ap.add_argument('--strict',action='store_true')
    ns=ap.parse_args(); root=ns.artifact.resolve()
    report={'schema_version':1,'artifact':root.name,'checks':{},'issues':[]}
    files=[]; symlinks=[]
    for p in sorted(root.rglob('*')):
        if p.is_symlink(): symlinks.append(safe_rel(root,p)); continue
        if p.is_file() and '__pycache__' not in p.parts and not p.name.endswith('.pyc'):
            files.append(p)
    if symlinks: report['issues'].append(f'symbolic links present: {symlinks}')
    report['checks']['inventory']={'files':len(files),'bytes':sum(p.stat().st_size for p in files),'symlinks':symlinks}
    json_errors=[]
    for p in files:
        if p.suffix.lower()=='.json':
            try: check_json(p)
            except Exception as e: json_errors.append({'file':safe_rel(root,p),'error':str(e)})
    if json_errors: report['issues'].append(f'{len(json_errors)} JSON parse/canonicality errors')
    report['checks']['json']={'count':sum(p.suffix.lower()=='.json' for p in files),'errors':json_errors}
    csv_errors=[]
    for p in files:
        if p.suffix.lower()=='.csv':
            try:
                with p.open(newline='',encoding='utf-8') as f:
                    rows=list(csv.reader(f))
                widths={len(r) for r in rows}
                if len(widths)>1: raise ValueError(f'non-rectangular widths {sorted(widths)}')
            except Exception as e: csv_errors.append({'file':safe_rel(root,p),'error':str(e)})
    if csv_errors: report['issues'].append(f'{len(csv_errors)} CSV errors')
    report['checks']['csv']={'count':sum(p.suffix.lower()=='.csv' for p in files),'errors':csv_errors}
    py_errors=[]
    for p in files:
        if p.suffix=='.py':
            try: ast.parse(p.read_text(encoding='utf-8'),filename=str(p))
            except Exception as e: py_errors.append({'file':safe_rel(root,p),'error':str(e)})
    if py_errors: report['issues'].append(f'{len(py_errors)} Python syntax errors')
    report['checks']['python']={'count':sum(p.suffix=='.py' for p in files),'errors':py_errors}
    # ZIP/JAR structural integrity; CRC test reads every member.
    zip_errors=[]; zip_count=0
    for p in files:
        if p.suffix.lower() in {'.zip','.jar'}:
            zip_count+=1
            try:
                with zipfile.ZipFile(p) as z:
                    bad=z.testzip()
                    if bad: raise ValueError(f'bad CRC member {bad}')
                    for n in z.namelist():
                        q=Path(n.replace('\\','/'))
                        if q.is_absolute() or '..' in q.parts: raise ValueError(f'unsafe member {n!r}')
            except Exception as e: zip_errors.append({'file':safe_rel(root,p),'error':str(e)})
    if zip_errors: report['issues'].append(f'{len(zip_errors)} archive integrity/safety errors')
    report['checks']['archives']={'count':zip_count,'errors':zip_errors}
    report['checks']['paper']=paper_audit(ns.paper.resolve()) if ns.paper else {'present':False,'issues':[]}
    report['issues'].extend(report['checks']['paper'].get('issues',[]))
    # Incorporate independent retained audits when present.
    crossref_path=root/'docs'/'reference-crossref-audit.json'
    if crossref_path.exists():
        try:
            cr=json.loads(crossref_path.read_text(encoding='utf-8'))
            statuses={}
            for r in cr.get('records',[]): statuses[r.get('status','UNKNOWN')]=statuses.get(r.get('status','UNKNOWN'),0)+1
            blocking=[r for r in cr.get('records',[]) if r.get('status') in {'TITLE_MISMATCH','PARSE_ERROR'}]
            report['checks']['crossref']={'statuses':statuses,'blocking':blocking}
            if blocking: report['issues'].append(f'{len(blocking)} confirmed Crossref title/parse mismatches')
        except Exception as e:
            report['issues'].append(f'cannot parse Crossref audit: {e}')
    language_path=root/'docs'/'claim-language-audit.json'
    if language_path.exists():
        try:
            la=json.loads(language_path.read_text(encoding='utf-8'))
            report['checks']['claim_language']={'blocking_hits':la.get('blocking_hits',[])}
            if la.get('blocking_hits'): report['issues'].append(f"{len(la['blocking_hits'])} blocking overclaim-language hits")
        except Exception as e: report['issues'].append(f'cannot parse claim-language audit: {e}')
    baseline_path=root/'results'/'information-baselines.json'
    if baseline_path.exists():
        try:
            ib=json.loads(baseline_path.read_text(encoding='utf-8'))
            expected={'archive_count':107,'unordered_pair_count':5671,'collision_pair_count':40,'selected_group_count':4,'enumerated_order_count':42,'output_class_count':14,'local_overapprox_region_count':100}
            mism={k:{'actual':ib.get(k),'expected':v} for k,v in expected.items() if ib.get(k)!=v}
            report['checks']['information_baselines']={'mismatches':mism}
            if mism: report['issues'].append(f'information-baseline retained result mismatch: {mism}')
        except Exception as e: report['issues'].append(f'cannot parse information-baseline result: {e}')
    infozip_path=root/'results'/'infozip-validation.json'
    if infozip_path.exists():
        try:
            iz=json.loads(infozip_path.read_text(encoding='utf-8'))
            expected={'frame_archive_count':107,'group_count':4,'order_count':42,'mismatch_count':0}
            mism={k:{'actual':iz.get(k),'expected':v} for k,v in expected.items() if iz.get(k)!=v}
            report['checks']['infozip_validation']={'mismatches':mism,'engine':iz.get('engine')}
            if mism: report['issues'].append(f'Info-ZIP retained validation mismatch: {mism}')
        except Exception as e: report['issues'].append(f'cannot parse Info-ZIP validation: {e}')
    # Claim index is regenerated and its strict status incorporated.
    claim_script=root/'scripts'/'audit_claims.py'
    claim_cmd=[sys.executable,str(claim_script),'--artifact',str(root)]
    if ns.paper: claim_cmd += ['--paper',str(ns.paper.resolve())]
    claim_cmd += ['--strict']
    cp=run(claim_cmd,cwd=root)
    report['checks']['claim_index']={'returncode':cp.returncode,'output':cp.stdout[-4000:]}
    if cp.returncode: report['issues'].append('claim-evidence index has missing anchors or parse errors')
    report['status']='PASS' if not report['issues'] else 'FAIL'
    oj=ns.output_json or root/'docs'/'release-audit.json'; om=ns.output_md or root/'docs'/'release-audit.md'
    oj.parent.mkdir(parents=True,exist_ok=True); om.parent.mkdir(parents=True,exist_ok=True)
    oj.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    lines=['# Release audit','',f"**Status: {report['status']}**",'',
           'This gate checks release integrity and traceability. It is not peer review and does not certify claims outside the stated model.','',
           '| Check | Result |','|---|---|',
           f"| Files | {report['checks']['inventory']['files']} files; {report['checks']['inventory']['bytes']} bytes |",
           f"| Strict JSON | {report['checks']['json']['count']} files; {len(json_errors)} errors |",
           f"| Rectangular UTF-8 CSV | {report['checks']['csv']['count']} files; {len(csv_errors)} errors |",
           f"| Python syntax | {report['checks']['python']['count']} files; {len(py_errors)} errors |",
           f"| ZIP/JAR CRC and member safety | {zip_count} archives; {len(zip_errors)} errors |",
           f"| Claim anchors | {'PASS' if cp.returncode==0 else 'FAIL'} |"]
    pa=report['checks']['paper']
    if pa.get('present'):
        lines.append(f"| Bibliography | {pa.get('bibliography_entries',0)} entries; {len(pa.get('missing_keys',[]))} missing keys; {len(pa.get('uncited_keys',[]))} uncited |")
    if report['issues']:
        lines += ['','## Blocking issues','']+[f'- {x}' for x in report['issues']]
    else: lines += ['','No blocking issue was found by this mechanical gate.']
    om.write_text('\n'.join(lines)+'\n')
    print(report['status'])
    return 2 if ns.strict and report['issues'] else 0
if __name__=='__main__': raise SystemExit(main())
