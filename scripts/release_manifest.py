#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib
from pathlib import Path
EXCLUDE={'RELEASE-MANIFEST.sha256'}
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def files(root):
 for p in sorted(root.rglob('*')):
  if not p.is_file() or p.is_symlink():continue
  rel=p.relative_to(root).as_posix()
  if p.name in EXCLUDE or '__pycache__' in p.parts or p.suffix=='.pyc' or '/reproduced/' in '/'+rel+'/':continue
  yield rel,p
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument('--output',type=Path);ap.add_argument('--verify',action='store_true');ns=ap.parse_args();root=ns.root.resolve();out=ns.output or root/'RELEASE-MANIFEST.sha256'
 if ns.verify:
  bad=[]
  for line in out.read_text().splitlines():
   if not line.strip():continue
   digest,rel=line.split('  ',1);p=root/rel
   if not p.is_file() or sha(p)!=digest:bad.append(rel)
  current={r for r,_ in files(root)};listed={line.split('  ',1)[1] for line in out.read_text().splitlines() if line.strip()}
  bad+=sorted(current-listed);bad+=['missing:'+x for x in sorted(listed-current)]
  if bad:raise SystemExit('manifest mismatch: '+repr(bad[:20]))
  print('manifest: PASS');return
 out.write_text(''.join(f'{sha(p)}  {rel}\n' for rel,p in files(root)))
if __name__=='__main__':main()
