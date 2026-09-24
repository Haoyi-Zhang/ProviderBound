#!/usr/bin/env python3
"""Locate scope-sensitive language in paper sources without rewriting prose."""
from pathlib import Path
import argparse,json,re
RULES=[
 ('ecosystem-representative',r'(?<!not )(?<!non[- ])representative (?:of|sample|corpus)'),
 ('unqualified-real-world-generalization',r'generaliz(?:e|es|ed|able) to (?:real[- ]world|the ecosystem|android|java)'),
 ('legal-ownership-inference',r'(?:infer|identify|establish|prove)s? (?:the )?legal owner'),
 ('authorship-inference',r'(?:infer|identify|establish|prove)s? (?:the )?(?:author|authorship)'),
 ('all-build-systems',r'(?:all|any) build systems?'),
 ('complete-provider-certification',r'(?:certif|prove|guarantee)\w* (?:that )?(?:the )?provider (?:list|inventory) is complete'),
 ('android-model-overclaim',r'(?:model|handle|support|cover)s? (?:the )?(?:complete|full) android build'),
 ('performance-overclaim',r'\b(?:scalable|negligible overhead|production-ready|industrial-scale)\b'),
 ('acceptance-claim',r'\b(?:meets|satisfies|guarantees) (?:all )?(?:tosem|acm) (?:requirements|standards)\b'),
]
SENSITIVE=[r'\bfirst\b',r'\bnovel\b',r'\bguarantee\w*\b',r'\bcomplete\w*\b',r'\breal[- ]world\b',r'\bownership\b',r'\bAndroid\b']
def strip_comments(line):
 out='';i=0
 while i<len(line):
  if line[i]=='%' and (i==0 or line[i-1]!='\\'): break
  out+=line[i];i+=1
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--paper',type=Path,required=True);ap.add_argument('--output',type=Path);ap.add_argument('--strict',action='store_true');ns=ap.parse_args()
 hits=[];sensitive=[]
 for p in sorted(ns.paper.rglob('*.tex')):
  for no,line in enumerate(p.read_text(encoding='utf-8',errors='replace').splitlines(),1):
   code=strip_comments(line)
   for rid,pat in RULES:
    if re.search(pat,code,re.I):hits.append({'rule':rid,'file':str(p.relative_to(ns.paper)),'line':no,'text':code.strip()})
   if any(re.search(p,code,re.I) for p in SENSITIVE): sensitive.append({'file':str(p.relative_to(ns.paper)),'line':no,'text':code.strip()})
 report={'schema_version':1,'blocking_hits':hits,'sensitive_contexts':sensitive,
         'note':'Blocking rules are deliberately narrow. Sensitive contexts require human reading and are not automatic errors.'}
 out=ns.output or Path(__file__).resolve().parents[1]/'docs'/'claim-language-audit.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
 md=out.with_suffix('.md'); lines=['# Claim-language audit','',report['note'],'',f"Blocking hits: **{len(hits)}**",'']
 if hits:
  lines += ['| Rule | Source | Text |','|---|---|---|']+[f"| {x['rule']} | `{x['file']}:{x['line']}` | {x['text'].replace('|','\\|')} |" for x in hits]
 lines += ['','## Scope-sensitive contexts','', '| Source | Text |','|---|---|']+[f"| `{x['file']}:{x['line']}` | {x['text'].replace('|','\\|')} |" for x in sensitive]
 md.write_text('\n'.join(lines)+'\n')
 return 2 if ns.strict and hits else 0
if __name__=='__main__':raise SystemExit(main())
