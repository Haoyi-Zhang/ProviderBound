#!/usr/bin/env python3
"""Inventory executable tests that defend the parser/checker trust boundary."""
from __future__ import annotations
import argparse, ast, json, re
from pathlib import Path
from collections import defaultdict

ROOT=Path(__file__).resolve().parents[1]
CATEGORIES={
 'schema_malleability': ('unknown','duplicate','schema','version','hex','json','nonfinite','nan','infinity'),
 'path_canonicalization': ('traversal','absolute','backslash','nul','canonical','normaliz','path'),
 'order_and_inconsistency': ('cycle','order','topolog','inconsisten','constraint','no feasible'),
 'certificate_mutation': ('tamper','mutat','certificate','witness','counterfactual','replay','truncat'),
 'unsupported_semantics': ('unsupported','transform','relocat','manifest','service','native','dex'),
 'implementation_separation': ('checker','producer','oracle','independent','adapter','brute'),
}

def test_records():
    records=[]
    for p in ROOT.rglob('*.py'):
        if '__pycache__' in p.parts: continue
        try:
            src=p.read_text(encoding='utf-8')
            tree=ast.parse(src,filename=str(p))
        except Exception:
            continue
        lines=src.splitlines()
        for node in ast.walk(tree):
            if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)) and node.name.startswith('test'):
                end=getattr(node,'end_lineno',node.lineno)
                body='\n'.join(lines[node.lineno-1:end]).lower()
                records.append({'file':str(p.relative_to(ROOT)),'name':node.name,'line':node.lineno,'text':body})
    return records

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--strict',action='store_true'); args=ap.parse_args()
    records=test_records()
    cats=defaultdict(list)
    for rec in records:
        hay=(rec['name']+' '+rec['text']).lower()
        for cat,tokens in CATEGORIES.items():
            if any(t in hay for t in tokens):
                cats[cat].append({'file':rec['file'],'name':rec['name'],'line':rec['line']})
    result={
      'schema_version':1,
      'test_functions':len(records),
      'categories':{k:v for k,v in cats.items()},
      'category_counts':{k:len(cats.get(k,[])) for k in CATEGORIES},
      'limitations':[
        'This is a static evidence index; passing behavior is established by the clean release reproduction.',
        'Token-based categorization is conservative and is not itself a proof of test adequacy.',
        'The archive-safety audit separately checks duplicate names, path aliases, encryption, and symbolic links in the retained frame.'
      ]
    }
    missing=[k for k in ('schema_malleability','path_canonicalization','order_and_inconsistency','certificate_mutation') if not cats.get(k)]
    result['release_blockers']=([f'missing category: {k}' for k in missing] + ([f'only {len(records)} tests; expected at least 39'] if len(records)<39 else []))
    (ROOT/'docs').mkdir(exist_ok=True)
    (ROOT/'docs'/'security-test-evidence.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    md=['# Security and Tamper-Test Evidence','',f"The artifact contains **{len(records)}** statically discoverable test functions. Clean reproduction executes the project test stage; this file indexes tests relevant to the untrusted-input and untrusted-certificate boundary.",'']
    for cat in CATEGORIES:
        vals=cats.get(cat,[])
        md += [f"## {cat.replace('_',' ').title()}",'',f"Matched tests: **{len(vals)}**",'']
        md += [f"- `{v['file']}:{v['line']}` — `{v['name']}`" for v in vals]
        md += ['']
    md += ['## Interpretation',''] + [f'- {x}' for x in result['limitations']]
    if result['release_blockers']:
        md += ['','## Release blockers','']+[f'- {x}' for x in result['release_blockers']]
    (ROOT/'docs'/'security-test-evidence.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
    return 2 if args.strict and result['release_blockers'] else 0
if __name__=='__main__': raise SystemExit(main())
