#!/usr/bin/env python3
"""Build a machine-readable claim-to-evidence index from retained result files.

The script never recomputes or copies a claimed number into evidence.  It scans
JSON and CSV records, records exact value locations, and reports claims for which
no machine-readable occurrence exists.  Textual paper occurrences are indexed
separately and never count as empirical evidence.
"""
from __future__ import annotations
import argparse, csv, json, re, sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Iterable

@dataclass(frozen=True)
class Claim:
    id: str
    statement: str
    values: tuple[Any, ...]
    scope: str

CLAIMS = (
    Claim("C-EXACT-LABELS", "Exhaustive normalized owner-label projections checked", (676354,), "finite models with one to three providers"),
    Claim("C-FRAME", "Frozen public sampling frame", (107, 37, 5671), "one preserved Debian Java-archive environment"),
    Claim("C-COLLISIONS", "Providers and unordered pairs with non-metadata collisions", (43, 40), "the frozen 107-archive frame"),
    Claim("C-MULTI", "Real multi-provider groups, concrete orders, and observable output classes", (4, 42, 14), "selected connected conflict components; every permutation built"),
    Claim("C-PAIR-BUILDS", "Two-order real archive builds", (80,), "40 colliding pairs"),
    Claim("C-OBS", "Region and colliding-region observations", (165630, 8156), "80 pair builds"),
    Claim("C-HIDDEN", "Content-identical outputs with changed hidden provider winners", (3471,), "equal-content collisions at module-provider granularity"),
    Claim("C-COUPLING", "Locally equal-content regions resolved by a different-content global-order constraint", (100,), "the retained mixed public case"),
    Claim("C-SCALE", "Largest retained scale probe", (300, 20000, 8602784), "synthetic stress probe; not an ecosystem estimate"),
)

TEXT_SUFFIXES={'.tex','.md','.txt','.bib'}

def json_leaves(value: Any, pointer: str='') -> Iterable[tuple[str, Any]]:
    if isinstance(value, dict):
        for k,v in value.items():
            esc=str(k).replace('~','~0').replace('/','~1')
            yield from json_leaves(v, pointer+'/'+esc)
    elif isinstance(value, list):
        for i,v in enumerate(value):
            yield from json_leaves(v, pointer+'/'+str(i))
    elif isinstance(value, (str,int,float,bool)) or value is None:
        yield pointer or '/', value

def norm_num(v: Any):
    if isinstance(v, bool): return None
    if isinstance(v, int): return v
    if isinstance(v, float) and v.is_integer(): return int(v)
    if isinstance(v, str):
        s=v.strip().replace(',','')
        if re.fullmatch(r'-?\d+',s): return int(s)
    return None

def scan_machine(root: Path):
    hits: dict[int,list[dict[str,Any]]] = {}
    parse_errors=[]
    for p in sorted(root.rglob('*')):
        if not p.is_file(): continue
        rel=p.relative_to(root).as_posix()
        if any(part in {'.git','__pycache__','reproduced'} for part in p.parts): continue
        if p.suffix.lower()=='.json':
            try: obj=json.loads(p.read_text(encoding='utf-8'))
            except Exception as e:
                parse_errors.append({'file':rel,'error':str(e)}); continue
            for ptr,v in json_leaves(obj):
                n=norm_num(v)
                if n is not None: hits.setdefault(n,[]).append({'file':rel,'location':ptr,'value':v,'format':'json'})
        elif p.suffix.lower()=='.csv':
            try:
                with p.open(newline='',encoding='utf-8') as f:
                    rd=csv.DictReader(f)
                    for rowno,row in enumerate(rd,start=2):
                        for col,v in row.items():
                            n=norm_num(v)
                            if n is not None: hits.setdefault(n,[]).append({'file':rel,'location':f'row {rowno}, column {col}','value':v,'format':'csv'})
            except Exception as e: parse_errors.append({'file':rel,'error':str(e)})
    return hits, parse_errors

def scan_text(roots: list[Path], values:set[int]):
    out={v:[] for v in values}
    for root in roots:
        if not root.exists(): continue
        for p in sorted(root.rglob('*')):
            if not p.is_file() or p.suffix.lower() not in TEXT_SUFFIXES: continue
            try: lines=p.read_text(encoding='utf-8',errors='replace').splitlines()
            except Exception: continue
            for i,line in enumerate(lines,1):
                stripped=line.replace(',','')
                for v in values:
                    if re.search(rf'(?<!\d){re.escape(str(v))}(?!\d)',stripped):
                        out[v].append({'file':str(p.relative_to(root)),'line':i})
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--artifact',type=Path,default=Path(__file__).resolve().parents[1])
    ap.add_argument('--paper',type=Path)
    ap.add_argument('--output-json',type=Path)
    ap.add_argument('--output-md',type=Path)
    ap.add_argument('--strict',action='store_true')
    ns=ap.parse_args()
    root=ns.artifact.resolve()
    values={int(v) for c in CLAIMS for v in c.values if isinstance(v,int)}
    machine, errors=scan_machine(root)
    text=scan_text([ns.paper.resolve()] if ns.paper else [],values)
    rows=[]; missing=[]
    for c in CLAIMS:
        ev={str(v):machine.get(int(v),[]) for v in c.values}
        absent=[v for v in c.values if not ev[str(v)]]
        if absent: missing.append({'claim':c.id,'values':absent})
        rows.append({**asdict(c),'values':list(c.values),'machine_evidence':ev,
                     'paper_occurrences':{str(v):text.get(int(v),[]) for v in c.values},
                     'status':'PASS' if not absent else 'MISSING'})
    report={'schema_version':1,'artifact_root':root.name,'claims':rows,
            'machine_parse_errors':errors,'missing':missing,
            'interpretation':('An exact value occurrence is a traceability aid, not proof by itself. '
                              'The reproduction pipeline remains the source of recomputation.')}
    oj=ns.output_json or root/'docs'/'claim-evidence-index.json'
    om=ns.output_md or root/'docs'/'claim-evidence-index.md'
    oj.parent.mkdir(parents=True,exist_ok=True); om.parent.mkdir(parents=True,exist_ok=True)
    oj.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    lines=['# Claim–evidence index','',report['interpretation'],'',
           '| ID | Scoped claim | Values | Machine evidence | Status |','|---|---|---:|---|---|']
    for r in rows:
        refs=[]
        for v in r['values']:
            locs=r['machine_evidence'][str(v)]
            if locs:
                shown='; '.join(f"`{x['file']}:{x['location']}`" for x in locs[:3])
                if len(locs)>3: shown+=f"; +{len(locs)-3} more"
            else: shown='—'
            refs.append(f"{v}: {shown}")
        lines.append(f"| {r['id']} | {r['statement']} — *{r['scope']}* | {', '.join(map(str,r['values']))} | {'<br>'.join(refs)} | {r['status']} |")
    if errors:
        lines += ['','## Parse errors','']+[f"- `{e['file']}`: {e['error']}" for e in errors]
    if missing:
        lines += ['','## Missing machine-readable anchors','',
                  'These omissions must be resolved before using the corresponding number in the paper.','']
        lines += [f"- {m['claim']}: {m['values']}" for m in missing]
    else:
        lines += ['','All registered quantitative claims have at least one exact machine-readable anchor.']
    om.write_text('\n'.join(lines)+'\n')
    if ns.strict and (missing or errors): return 2
    return 0
if __name__=='__main__': raise SystemExit(main())
