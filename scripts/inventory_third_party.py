#!/usr/bin/env python3
"""Inventory redistributed archive inputs and available license/provenance records."""
from pathlib import Path
import argparse,hashlib,json,re

def sha(p):
 h=hashlib.sha256();
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--artifact',type=Path,default=Path(__file__).resolve().parents[1]); ns=ap.parse_args()
 root=ns.artifact.resolve()
 inputs=root/'inputs'
 if not inputs.exists(): inputs=root
 jars=[]
 for p in sorted(inputs.rglob('*')):
  if p.is_file() and p.suffix.lower() in {'.jar','.zip'}:
   jars.append({'path':p.relative_to(root).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
 records=[]
 for p in sorted(inputs.rglob('*')):
  if p.is_file() and (re.search(r'(license|licence|copying|copyright|notice)',p.name,re.I) or p.suffix.lower() in {'.copyright'}):
   records.append({'path':p.relative_to(root).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
 manifests=[]
 for p in sorted(inputs.rglob('*')):
  if p.is_file() and p.suffix.lower() in {'.json','.csv','.md','.txt'}:
   try:t=p.read_text(encoding='utf-8',errors='ignore').lower()
   except:continue
   score=sum(k in t for k in ('sha256','source package','upstream','license','copyright'))
   if score>=2: manifests.append(p.relative_to(root).as_posix())
 report={'schema_version':1,'archive_inputs':jars,'license_notice_records':records,
         'candidate_provenance_manifests':manifests,
         'legal_note':('This inventory is not legal advice. Presence of a notice does not by itself satisfy all redistribution duties; '
                       'submitting authors must review corresponding-source and notice requirements before public release.')}
 out=root/'docs'/'third-party-input-inventory.json'; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
 md=['# Third-party input inventory','',report['legal_note'],'',f"- Archive inputs: {len(jars)}",f"- License/notice records: {len(records)}",f"- Candidate provenance manifests: {len(manifests)}",'',
     '## Archive inputs','', '| Path | Bytes | SHA-256 |','|---|---:|---|']
 md += [f"| `{x['path']}` | {x['bytes']} | `{x['sha256']}` |" for x in jars]
 md += ['','## License and notice records','', '| Path | Bytes | SHA-256 |','|---|---:|---|']
 md += [f"| `{x['path']}` | {x['bytes']} | `{x['sha256']}` |" for x in records]
 md += ['','## Candidate provenance manifests','']+[f"- `{x}`" for x in manifests]
 (root/'docs'/'third-party-input-inventory.md').write_text('\n'.join(md)+'\n')
 return 0
if __name__=='__main__': raise SystemExit(main())
