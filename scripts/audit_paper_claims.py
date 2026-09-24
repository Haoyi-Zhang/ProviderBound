#!/usr/bin/env python3
from pathlib import Path
import argparse,json,re,subprocess
REQUIRED={
 'label-partition enumeration':r'676\s*[,{}\\]*\s*354',
 'complete archive frame':r'107[- ]archive|107\s+(?:public\s+)?(?:JAR|archive)',
 'upstream projects':r'37\s+(?:upstream[- ]project|projects)',
 'all unordered pairs':r'5\s*[,{}\\]*\s*671',
 'multi-provider orders':r'42\s+(?:orders|permutations)',
 'multi-provider output classes':r'14\s+(?:observable\s+)?output classes',
 'hidden equal-byte reversals':r'3\s*[,{}\\]*\s*471',
 'global-coupling resolution':r'100\s+(?:mixed-case\s+)?regions',
 'caller supplied labels':r'caller[- ]supplied label',
 'not legal ownership':r'not (?:authorship or )?legal ownership|neither inferred authorship nor legal ownership',
 'finite-frame generalization':r'(?:not a random or representative|does not estimate prevalence|finite-population)',
 'entry-map equality':r'entry[- ]to[- ](?:uncompressed[- ])?byte map|not ZIP container serialization',
 'Info-ZIP validation':r'Info-ZIP|unzip\s*-n',
 'metadata sensitivity':r'Metadata sensitivity|metadata-only',
}
FORBIDDEN={
 'ecosystem representativeness claim':r'\b(?:is|are|constitutes?) (?:a )?representative (?:sample|corpus)',
 'legal owner inference':r'\b(?:infer|identify|prove|establish)(?:s|d|ing)? (?:the )?legal owner',
 'provider-list completeness guarantee':r'\b(?:prove|certif|guarantee)\w* (?:the )?provider (?:list|inventory) (?:is )?complete',
 'full Android model claim':r'\b(?:model|support|cover)\w* (?:the )?(?:complete|full) Android build',
 'acceptance guarantee':r'\bguarantee\w* (?:TOSEM|ACM) (?:acceptance|compliance)',
}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--paper',type=Path,required=True);ap.add_argument('--output',type=Path);ap.add_argument('--strict',action='store_true');ns=ap.parse_args();paper=ns.paper.resolve()
 tex='\n'.join(p.read_text(encoding='utf-8',errors='replace') for p in paper.rglob('*.tex'))
 missing={k:v for k,v in REQUIRED.items() if not re.search(v,tex,re.I|re.S)}
 forbidden={k:re.findall(v,tex,re.I|re.S)[:10] for k,v in FORBIDDEN.items() if re.search(v,tex,re.I|re.S)}
 pages=None;pdfs=sorted(paper.rglob('*.pdf'),key=lambda p:p.stat().st_mtime)
 if pdfs:
  info=subprocess.check_output(['pdfinfo',str(pdfs[-1])],text=True);m=re.search(r'^Pages:\s+(\d+)',info,re.M);pages=int(m.group(1)) if m else None
 report={'schema_version':1,'required':{k:k not in missing for k in REQUIRED},'missing':missing,'forbidden_hits':forbidden,'pages':pages,
         'status':'PASS' if not missing and not forbidden and pages==36 else 'FAIL'}
 out=ns.output or Path(__file__).resolve().parents[1]/'docs'/'paper-claim-audit.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
 md=['# Paper claim audit','',f"**Status: {report['status']}**",'',f"Pages: {pages}",'','| Required element | Present |','|---|---|']+[f"| {k} | {'yes' if v else 'no'} |" for k,v in report['required'].items()]
 if forbidden:md+=['','## Forbidden overclaims','']+[f'- {k}' for k in forbidden]
 out.with_suffix('.md').write_text('\n'.join(md)+'\n')
 if ns.strict and report['status']!='PASS':return 2
 return 0
if __name__=='__main__':raise SystemExit(main())
