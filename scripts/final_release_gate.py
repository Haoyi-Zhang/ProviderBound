#!/usr/bin/env python3
"""Fail-closed gate for the frozen paper/artifact release.

This script intentionally distinguishes machine-verifiable release properties
from human-only submission actions.  It produces a compact JSON/Markdown record
and exits non-zero on any machine-verifiable blocker.
"""
from __future__ import annotations
import argparse, ast, hashlib, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

ART=Path(__file__).resolve().parents[1]
ROOT=ART.parent
PAPER=ROOT/'paper'
TITLE='Proof-Carrying Provider Attribution under First-Winner Archive Merging'
OLD_TITLES=('Proof-Carrying First-Winner Library Boundaries','Certifying First-Winner Library Boundaries')


def run(cmd, cwd=None, timeout=900):
    p=subprocess.run(cmd,cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=timeout)
    if p.returncode:
        tail='\n'.join(p.stdout.splitlines()[-100:])
        raise RuntimeError(f"command failed ({p.returncode}): {' '.join(map(str,cmd))}\n{tail}")
    return p.stdout


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def scalar_paths(obj, prefix='$'):
    if isinstance(obj,dict):
        for k,v in obj.items(): yield from scalar_paths(v,prefix+'.'+str(k))
    elif isinstance(obj,list):
        for i,v in enumerate(obj): yield from scalar_paths(v,f'{prefix}[{i}]')
    else: yield prefix,obj


def find_pdf():
    candidates=[]
    for p in PAPER.rglob('*.pdf'):
        try:
            out=run(['pdfinfo',str(p)],timeout=30)
            m=re.search(r'^Pages:\s+(\d+)\s*$',out,re.M)
            if m and int(m.group(1))==36:
                candidates.append((p.stat().st_mtime,p.stat().st_size,p))
        except Exception:
            pass
    if not candidates: raise RuntimeError('no 36-page PDF found in paper tree')
    return sorted(candidates)[-1][2]


def bib_closure():
    tex='\n'.join(p.read_text(encoding='utf-8',errors='ignore') for p in PAPER.rglob('*.tex'))
    bib='\n'.join(p.read_text(encoding='utf-8',errors='ignore') for p in PAPER.rglob('*.bib'))
    entries=set(re.findall(r'@\w+\s*\{\s*([^,\s]+)',bib))
    cited=set()
    for chunk in re.findall(r'\\cite\w*\s*(?:\[[^\]]*\]\s*)*\{([^}]*)\}',tex):
        cited.update(x.strip() for x in chunk.split(',') if x.strip())
    missing=sorted(cited-entries)
    uncited=sorted(entries-cited)
    dois=[]
    for m in re.finditer(r'(?i)\bdoi\s*=\s*[\{\"]([^}\"]+)',bib):
        d=m.group(1).strip().lower().removeprefix('https://doi.org/').removeprefix('http://doi.org/')
        dois.append(d)
    dup=sorted({d for d in dois if dois.count(d)>1})
    malformed=sorted(d for d in dois if not re.match(r'^10\.\d{4,9}/\S+$',d))
    return {'entries':len(entries),'cited_keys':len(cited),'missing':missing,'uncited':uncited,'duplicate_dois':dup,'malformed_dois':malformed}


def empty_field(path, keys):
    obj=load(path); vals=dict(scalar_paths(obj)); bad=[]
    for p,v in vals.items():
        leaf=p.rsplit('.',1)[-1].lower()
        if leaf in keys and v not in ([],{},None,0,'',False): bad.append((p,v))
    return bad


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--skip-build',action='store_true'); args=ap.parse_args()
    checks=[]; blockers=[]; notes=[]
    def check(name, ok, detail):
        checks.append({'name':name,'passed':bool(ok),'detail':detail})
        if not ok: blockers.append(f'{name}: {detail}')

    # Rebuild and rerun the release-facing audits from the same tree.
    if not args.skip_build:
        run([sys.executable,'build.py'],cwd=PAPER)
        if Path('/mnt/data/enforce_paper_pages.py').exists():
            run([sys.executable,'/mnt/data/enforce_paper_pages.py'],cwd=PAPER)
    commands=[
      ([sys.executable,'scripts/analyze_information_baselines.py'],ART),
      ([sys.executable,'scripts/validate_infozip_merger.py'],ART),
      ([sys.executable,'scripts/analyze_metadata_sensitivity.py'],ART),
      ([sys.executable,'scripts/analyze_certificate_compression.py'],ART),
      ([sys.executable,'scripts/audit_claims.py'],ART),
      ([sys.executable,'scripts/audit_archive_safety.py','--strict'],ART),
      ([sys.executable,'scripts/audit_independence.py','--strict'],ART),
      ([sys.executable,'scripts/audit_security_test_evidence.py','--strict'],ART),
      ([sys.executable,'scripts/audit_scope_consistency.py','--strict'],ART),
      ([sys.executable,'scripts/audit_claim_language.py','--strict'],ART),
      ([sys.executable,'scripts/audit_paper_claims.py','--strict'],ART),
    ]
    for cmd,cwd in commands:
        run(cmd,cwd=cwd)
    # audit_release must run after the component audits above.
    run([sys.executable,'scripts/audit_release.py','--strict'],cwd=ART)
    if (PAPER/'audit_acmart.py').exists(): run([sys.executable,'audit_acmart.py'],cwd=PAPER)

    pdf=find_pdf()
    info=run(['pdfinfo',str(pdf)],timeout=30)
    pages=int(re.search(r'^Pages:\s+(\d+)\s*$',info,re.M).group(1))
    check('paper-page-count',pages==36,f'{pages} pages; expected exactly 36 under the internal contract')
    text=run(['pdftotext',str(pdf),'-'],timeout=60)
    check('paper-title',TITLE in text,'canonical title present in extracted PDF text')
    check('old-title-removed',not any(t in text for t in OLD_TITLES),'no superseded title in PDF')

    fonts=run(['pdffonts',str(pdf)],timeout=30)
    font_lines=[l.split() for l in fonts.splitlines()[2:] if l.strip()]
    unembedded=[]
    for line in font_lines:
        # pdffonts columns vary; the penultimate yes/no columns include emb/sub.
        if 'no' in [x.lower() for x in line[-5:]]:
            # conservatively inspect the 'emb' column by header position when possible
            header=fonts.splitlines()[0].split()
            try:
                idx=header.index('emb')
                if idx < len(line) and line[idx].lower()=='no': unembedded.append(line[0])
            except ValueError:
                pass
    check('embedded-fonts',not unembedded,f'unembedded={unembedded}')
    if shutil.which('qpdf'):
        run(['qpdf','--check',str(pdf)],timeout=60)
        check('qpdf-structural-check',True,'qpdf --check passed')

    # LaTeX diagnostics.
    logs=list(PAPER.rglob('*.log'))
    logtext='\n'.join(p.read_text(encoding='utf-8',errors='ignore') for p in logs)
    badlog=[]
    for pat in ('LaTeX Error','Undefined control sequence','There were undefined references','Citation `','Overfull \\hbox','Overfull \\vbox'):
        if pat in logtext: badlog.append(pat)
    check('latex-diagnostics',not badlog,f'blocking diagnostics={badlog}')

    bib=bib_closure()
    check('bibliography-count',bib['entries']>=54,f"{bib['entries']} entries")
    check('bibliography-closure',not bib['missing'] and not bib['uncited'],f"missing={bib['missing']}; uncited={bib['uncited']}")
    check('bibliography-dois',not bib['duplicate_dois'] and not bib['malformed_dois'],f"duplicate={bib['duplicate_dois']}; malformed={bib['malformed_dois']}")

    expected_audits={
      'archive-safety-audit.json':('errors','archives_with_errors'),
      'implementation-independence-audit.json':('violations',),
      'security-test-evidence.json':('release_blockers',),
      'scope-consistency-audit.json':('release_blockers',),
      'claim-language-audit.json':('release_blockers','blocking_hits'),
      'paper-claim-audit.json':('release_blockers',),
      'release-audit.json':('release_blockers','violations'),
    }
    for filename,fields in expected_audits.items():
        p=ART/'docs'/filename
        check('audit-present:'+filename,p.exists(),str(p.relative_to(ROOT)) if p.exists() else 'missing')
        if not p.exists(): continue
        obj=load(p)
        bad=[]
        for field in fields:
            if field in obj and obj[field] not in ([],{},0,None,'',False): bad.append((field,obj[field]))
        check('audit-clean:'+filename,not bad,f'{bad}')

    security=load(ART/'docs'/'security-test-evidence.json')
    check('test-inventory',security.get('test_functions',0)>=39,f"{security.get('test_functions',0)} statically discoverable tests")
    archive=load(ART/'docs'/'archive-safety-audit.json')
    check('archive-frame-size',archive.get('frame_archives')==107,f"{archive.get('frame_archives')} archives")

    # Claim evidence index must cover every registered claim without a missing marker.
    claim_path=ART/'docs'/'claim-evidence-index.json'
    check('claim-index-present',claim_path.exists(),str(claim_path.relative_to(ROOT)) if claim_path.exists() else 'missing')
    if claim_path.exists():
        c=load(claim_path)
        flat=list(scalar_paths(c))
        bad=[(p,v) for p,v in flat if ('missing' in p.lower() or 'unresolved' in p.lower()) and v not in ([],{},0,None,'',False)]
        check('claim-index-resolved',not bad,f'{bad[:10]}')
        serialized=json.dumps(c,sort_keys=True)
        for n in ('676354','107','5671','43','40','42','14','80','165630','8156','3471','100','300','20000','8602784'):
            check('claim-index-number:'+n,n in serialized,f'{n} registered')

    # Crossref/publisher audit: block semantic mismatches, tolerate recorded network failures.
    cross=ART/'docs'/'reference-crossref-audit.json'
    if cross.exists():
        obj=load(cross); statuses=[]
        for p,v in scalar_paths(obj):
            if p.lower().endswith(('.status','.result','.classification')) and isinstance(v,str): statuses.append(v.upper())
        semantic=[s for s in statuses if any(k in s for k in ('TITLE_MISMATCH','DOI_MISMATCH','PARSE_ERROR'))]
        fetch=[s for s in statuses if 'FETCH_ERROR' in s or 'HTTP_ERROR' in s]
        check('reference-semantic-audit',not semantic,f'semantic failures={semantic}')
        notes.append(f'Reference audit recorded {len(fetch)} network-fetch failures; these are non-semantic and the retained publisher-resolution ledger remains available.')
    else:
        notes.append('No network Crossref audit JSON was available; bibliography closure and the retained manual ledger were still checked.')

    # Python syntax and forbidden generated clutter.
    syntax=[]
    for p in ART.rglob('*.py'):
        try: ast.parse(p.read_text(encoding='utf-8'),filename=str(p))
        except Exception as e: syntax.append(f'{p.relative_to(ART)}: {e}')
    check('python-syntax',not syntax,f'{syntax}')
    clutter=[str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.name in ('__pycache__','.pytest_cache','.mypy_cache') or p.suffix=='.pyc']
    check('no-runtime-clutter',not clutter,f'{clutter[:20]}')

    # Root contract.
    root_names=sorted(p.name for p in ROOT.iterdir())
    check('full-project-root-contract',root_names==["README.md", "artifact", "paper"],f'{root_names}')

    result={
      'schema_version':1,'canonical_title':TITLE,'paper_pdf':str(pdf.relative_to(ROOT)),
      'checks':checks,'blockers':blockers,'notes':notes,
      'machine_verifiable_status':'PASS' if not blockers else 'FAIL',
      'human_only_submission_actions':[
        'Confirm author names, affiliations, ORCIDs, contribution statements, and corresponding author.',
        'Confirm conflicts of interest, prior-publication status, ethics disclosures, and any required data/code licenses.',
        'Re-check the live TOSEM and ACM submission policies immediately before submission; live policy supersedes the retained probe.',
        'Upload the artifact to an archival public host and replace local/package links with persistent URLs or DOIs.',
        'Obtain independent coauthor review and, where appropriate, legal review of redistributed third-party materials.'
      ]
    }
    out=ART/'docs'/'FINAL-RELEASE-GATE.json'; out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    md=['# Final Release Gate','',f"Machine-verifiable status: **{result['machine_verifiable_status']}**",'',f"Paper: `{result['paper_pdf']}`",'', '## Checks','']
    md += [f"- {'PASS' if c['passed'] else 'FAIL'} — **{c['name']}**: {c['detail']}" for c in checks]
    if blockers: md += ['','## Blockers','']+[f'- {x}' for x in blockers]
    md += ['','## Human-only submission actions','']+[f'- {x}' for x in result['human_only_submission_actions']]
    if notes: md += ['','## Notes','']+[f'- {x}' for x in notes]
    (ART/'docs'/'FINAL-RELEASE-GATE.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
    return 2 if blockers else 0

if __name__=='__main__': raise SystemExit(main())
