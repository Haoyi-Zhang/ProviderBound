#!/usr/bin/env python3
from pathlib import Path
import argparse,json,re,subprocess
REQUIRED={
 'current provider cohort':r'43\s+(?:licensed public JAR providers|(?:experiment\s+)?providers)',
 'current collision pairs':r'40\s+(?:public JAR pairs|frozen collision pairs|colliding pairs)',
 'hidden equal-byte reversals':r'3\s*[,{}\\]*\s*471',
 'global-coupling resolution':r'100\s+(?:equal-byte observations|strict narrowings|provider-level narrowings)',
 'supplied owner labels':r'supplied inventories and owner labels|owner labels used here identify declared artifact roles',
 'not legal ownership':r'None of those possibilities licenses a legal-ownership claim',
 'bounded interpretation':r'not estimates of Android prevalence|not a universal scalability claim',
 'entry-map equality':r'complete output content map|entire observable content map',
 'current external builder':r'Apache Ant',
 'package-label negative result':r'zero\s+additional owner-set resolutions',
}
FORBIDDEN={
 'ecosystem representativeness claim':r'\b(?:is|are|constitutes?) (?:a )?representative (?:sample|corpus)',
 'legal owner inference':r'\b(?:infer|identify|prove|establish)(?:s|d|ing)? (?:the )?legal owner',
 'provider-list completeness guarantee':r'\b(?:prove|certif|guarantee)\w* (?:the )?provider (?:list|inventory) (?:is )?complete',
 'full Android model claim':r'\b(?:model|support|cover)\w* (?:the )?(?:complete|full) Android build',
 'acceptance guarantee':r'\bguarantee\w* (?:TOSEM|ACM) (?:acceptance|compliance)',
}
def document_sources(paper):
 """Read literal active inputs, not unrelated historical TeX documents."""
 paper=paper.resolve(); pending=[paper/'main.tex']; seen=set(); parts=[]
 while pending:
  path=pending.pop().resolve()
  if not path.is_relative_to(paper) or path in seen:
   if path in seen: continue
   raise ValueError('document input escapes paper tree')
  if len(seen)>=64: raise ValueError('document input bound')
  seen.add(path)
  source=path.read_text(encoding='utf-8')
  source=re.sub(r'(?<!\\)%[^\n]*','',source)
  parts.append(source)
  for name in re.findall(r'\\(?:input|include)\s*\{([^}]+)\}',source):
   if '\\' in name or '#' in name: raise ValueError('nonliteral document input')
   target=paper/name
   pending.append(target if target.suffix else target.with_suffix('.tex'))
 return '\n'.join(parts),sorted(p.relative_to(paper).as_posix() for p in seen)

def audit(paper):
 paper=paper.resolve()
 tex,sources=document_sources(paper)
 missing={k:v for k,v in REQUIRED.items() if not re.search(v,tex,re.I|re.S)}
 forbidden={k:re.findall(v,tex,re.I|re.S)[:10] for k,v in FORBIDDEN.items() if re.search(v,tex,re.I|re.S)}
 pages=None; pdf=paper/'main.pdf'
 if pdf.exists():
  completed=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,timeout=30)
  if completed.returncode: raise RuntimeError('pdfinfo failed')
  info=completed.stdout.decode('utf-8',errors='replace')
  m=re.search(r'^Pages:\s+(\d+)',info,re.M);pages=int(m.group(1)) if m else None
 return {'schema_version':2,'scope':'Active-manuscript text anchors and positive main.pdf page count; not scientific, source-PDF-binding or venue clearance.',
         'active_sources':sources,'pdf':'main.pdf','required':{k:k not in missing for k in REQUIRED},
         'missing':missing,'forbidden_hits':forbidden,'pages':pages,'fixed_page_ceiling':None,
         'status':'PASS' if not missing and not forbidden and pages is not None and pages>0 else 'FAIL'}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--paper',type=Path,required=True);ap.add_argument('--output',type=Path);ap.add_argument('--strict',action='store_true');ns=ap.parse_args();paper=ns.paper.resolve()
 report=audit(paper); pages=report['pages']; forbidden=report['forbidden_hits']
 out=ns.output or Path(__file__).resolve().parents[1]/'docs'/'paper-claim-audit.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
 md=['# Paper claim audit','',f"**Status: {report['status']}**",'',report['scope'],'',f"Pages: {pages}; no locked journal ceiling asserted.",'','| Required element | Present |','|---|---|']+[f"| {k} | {'yes' if v else 'no'} |" for k,v in report['required'].items()]
 if forbidden:md+=['','## Forbidden overclaims','']+[f'- {k}' for k in forbidden]
 out.with_suffix('.md').write_text('\n'.join(md)+'\n')
 if ns.strict and report['status']!='PASS':return 2
 return 0
if __name__=='__main__':raise SystemExit(main())
