#!/usr/bin/env python3
"""Detect cross-file title/scope drift and claims that exceed the frozen semantics."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PROJECT=ROOT.parent
NEW='Proof-Carrying Provider Attribution under First-Winner Archive Merging'
OLD=(
 'Proof-Carrying First-Winner Library Boundaries',
 'Certifying First-Winner Library Boundaries',
)
TEXT_SUFFIX={'.md','.tex','.txt','.bib','.csv','.json','.yml','.yaml','.cff'}
BLOCK_PATTERNS={
 'unqualified-real-world': re.compile(r'(?i)\breal[- ]world\s+(?:accuracy|coverage|validation|corpus|jars?)\b'),
 'guaranteed-accuracy': re.compile(r'(?i)\b(?:100%|perfect)\s+accuracy\b'),
 'legal-owner-claim': re.compile(r'(?i)\b(?:proves?|certifies?|determines?)\s+(?:the\s+)?(?:legal\s+)?owner(?:ship)?\b'),
 'complete-android-claim': re.compile(r'(?i)\b(?:supports?|models?|covers?|validates?)\s+(?:the\s+)?(?:complete|full|entire)\s+android\s+build'),
 'acceptance-guarantee': re.compile(r'(?i)\bguarantee(?:d|s)?\s+(?:publication|acceptance)\b'),
}
ALLOW_PARTS={'reference-crossref-audit.md','reference-crossref-audit.json','reference-publisher-resolution.md','reference-publisher-resolution.json'}

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--strict',action='store_true'); args=ap.parse_args()
 hits=[]; title_hits=[]; files=0
 for base in (PROJECT,):
  for p in base.rglob('*'):
   if not p.is_file() or p.suffix.lower() not in TEXT_SUFFIX: continue
   if any(x in p.parts for x in ('reproduced','__pycache__')): continue
   files+=1
   try: text=p.read_text(encoding='utf-8')
   except UnicodeDecodeError: continue
   rel=str(p.relative_to(PROJECT))
   for old in OLD:
    if old in text: title_hits.append({'file':rel,'old_title':old})
   if p.name in ALLOW_PARTS: continue
   for name,rx in BLOCK_PATTERNS.items():
    for m in rx.finditer(text):
     line=text.count('\n',0,m.start())+1
     hits.append({'file':rel,'line':line,'rule':name,'text':m.group(0)})
 result={
  'schema_version':1,'files_scanned':files,'canonical_title':NEW,
  'old_title_occurrences':title_hits,'blocking_scope_hits':hits,
  'release_blockers':[f"old title in {h['file']}" for h in title_hits]+[f"{h['rule']} in {h['file']}:{h['line']}" for h in hits],
  'note':'The mandated outer package name may contain legacy topic words; this audit concerns textual scientific claims and titles.'
 }
 (ROOT/'docs').mkdir(exist_ok=True)
 (ROOT/'docs'/'scope-consistency-audit.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
 md=['# Scope-Consistency Audit','',f"Canonical paper title: **{NEW}**",'',f"Text files scanned: **{files}**",f"Old-title occurrences: **{len(title_hits)}**",f"Blocking overclaim patterns: **{len(hits)}**",'',result['note']]
 if result['release_blockers']: md += ['','## Release blockers','']+[f'- {x}' for x in result['release_blockers']]
 (ROOT/'docs'/'scope-consistency-audit.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
 return 2 if args.strict and result['release_blockers'] else 0
if __name__=='__main__': raise SystemExit(main())
