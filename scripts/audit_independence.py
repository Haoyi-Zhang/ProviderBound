#!/usr/bin/env python3
"""Build and check the local Python import graph for independent validations."""
from __future__ import annotations
import argparse, ast, json
from pathlib import Path
from collections import defaultdict, deque

ROOT=Path(__file__).resolve().parents[1]


def module_name(path: Path) -> str:
    rel=path.relative_to(ROOT).with_suffix('')
    parts=list(rel.parts)
    if parts[-1]=='__init__': parts=parts[:-1]
    return '.'.join(parts)


def parse_imports(path: Path) -> set[str]:
    tree=ast.parse(path.read_text(encoding='utf-8'), filename=str(path))
    out=set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            out.update(a.name for a in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.module: out.add(node.module)
    return out


def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--strict', action='store_true'); args=ap.parse_args()
    files=[p for p in ROOT.rglob('*.py') if '__pycache__' not in p.parts and not any(x in p.parts for x in ('reproduced','reproduction'))]
    modules={module_name(p):p for p in files}
    tops={m.split('.')[0] for m in modules}
    imports={m:parse_imports(p) for m,p in modules.items()}
    local_edges={m:sorted(i for i in imps if i.split('.')[0] in tops) for m,imps in imports.items()}

    required_independent=[
        'scripts.analyze_information_baselines',
        'scripts.validate_infozip_merger',
        'scripts.audit_archive_safety',
    ]
    violations=[]
    details={}
    for name in required_independent:
        if name not in modules:
            violations.append({'module':name,'reason':'missing'})
            continue
        edges=local_edges.get(name,[])
        # importing another scripts.* or a source package is a common-mode dependency;
        # stdlib imports never appear in local_edges.
        bad=[e for e in edges if e != name]
        details[name]={'path':str(modules[name].relative_to(ROOT)), 'local_imports':edges}
        if bad:
            violations.append({'module':name,'reason':'local-import','imports':bad})

    # Record paths among likely producer/checker/oracle modules without imposing
    # name-based assumptions as a release failure.
    roles=defaultdict(list)
    for m in modules:
        low=m.lower()
        if any(k in low for k in ('producer','generate','infer','solver')): roles['producer'].append(m)
        if any(k in low for k in ('checker','verify','verifier')): roles['checker'].append(m)
        if any(k in low for k in ('oracle','bruteforce','brute_force','exhaust')): roles['oracle'].append(m)

    result={
        'schema_version':1,
        'python_files':len(files),
        'local_modules':len(modules),
        'required_independent_modules':details,
        'violations':violations,
        'role_candidates':{k:sorted(v) for k,v in roles.items()},
        'local_import_graph':local_edges,
        'interpretation':(
            'The literal-permutation information baseline, Info-ZIP validation, and archive-safety audit '
            'must not import the certificate producer, checker, or another project-local implementation. '
            'This check establishes implementation separation, not formal verification of Python itself.'
        ),
    }
    (ROOT/'docs').mkdir(exist_ok=True)
    (ROOT/'docs'/'implementation-independence-audit.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    md=['# Implementation-Independence Audit','',result['interpretation'],'']
    for name,d in details.items():
        md += [f"- `{name}`: local imports = `{', '.join(d['local_imports']) or 'none'}`"]
    md += ['',f"Release-blocking violations: **{len(violations)}**.",'']
    md += ['The report also records name-based producer/checker/oracle candidates for human review; those labels are not treated as proof of independence.']
    (ROOT/'docs'/'implementation-independence-audit.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
    return 2 if args.strict and violations else 0

if __name__=='__main__': raise SystemExit(main())
