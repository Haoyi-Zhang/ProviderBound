#!/usr/bin/env python3
"""Validate first-winner maps with the external Info-ZIP `unzip -n` engine.

`unzip -n` never overwrites an existing file. Sequential extraction therefore
implements first-winner merging without importing the producer, checker, Ant
adapter, or independent Python graph oracle used elsewhere.
"""
from __future__ import annotations
import argparse,hashlib,itertools,json,os,shutil,subprocess,tempfile,zipfile
from pathlib import Path

def canonical(name):
 name=name.replace('\\','/')
 if name.startswith('/') or '\x00' in name:raise ValueError(name)
 ps=name.split('/')
 if any(x in ('','.','..') for x in ps):raise ValueError(name)
 return '/'.join(ps)
def readjar(p):
 d={}
 with zipfile.ZipFile(p) as z:
  for i in z.infolist():
   if i.is_dir():continue
   try:n=canonical(i.filename)
   except ValueError:continue
   if n.upper().startswith('META-INF/'):continue
   if n in d:raise ValueError(f'duplicate {n} in {p}')
   d[n]=z.read(i)
 return d
def find_frame(root):
 cs=[]
 for d in [root]+[x for x in root.rglob('*') if x.is_dir()]:
  if sum(1 for p in d.rglob('*.jar') if p.is_file())==107:cs.append(d)
 if not cs:raise RuntimeError('107-JAR frame not found')
 return max(cs,key=lambda x:len(x.parts))
def comps(keys,maps):
 adj={k:set() for k in keys}
 for i,a in enumerate(keys):
  an=set(maps[a])
  for b in keys[i+1:]:
   if an & set(maps[b]):adj[a].add(b);adj[b].add(a)
 out=[];seen=set()
 for k in keys:
  if k in seen:continue
  q=[k];seen.add(k);c=[]
  while q:
   x=q.pop();c.append(x)
   for y in adj[x]:
    if y not in seen:seen.add(y);q.append(y)
  out.append(sorted(c))
 return out
def expected(order,maps):
 d={}
 for p in order:
  for n,b in maps[p].items():d.setdefault(n,b)
 return d
def extracted_map(d):
 out={}
 for p in sorted(d.rglob('*')):
  if not p.is_file():continue
  n=p.relative_to(d).as_posix()
  if n.upper().startswith('META-INF/'):continue
  out[n]=p.read_bytes()
 return out
def mapdigest(d):
 h=hashlib.sha256()
 for n in sorted(d):
  b=n.encode();h.update(len(b).to_bytes(4,'big'));h.update(b);h.update(len(d[n]).to_bytes(8,'big'));h.update(d[n])
 return h.hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--artifact',type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument('--frame',type=Path);ap.add_argument('--output',type=Path);ap.add_argument('--strict',action='store_true');ns=ap.parse_args()
 unzip=shutil.which('unzip')
 if not unzip:raise RuntimeError('Info-ZIP unzip is required')
 root=ns.artifact.resolve();frame=ns.frame.resolve() if ns.frame else find_frame(root/'inputs')
 jars=sorted(p for p in frame.rglob('*.jar') if p.is_file());ids={p.relative_to(frame).as_posix():p for p in jars};maps={k:readjar(p) for k,p in ids.items()}
 groups=[c for c in comps(sorted(ids),maps) if 3<=len(c)<=4]
 rows=[];mismatches=[]
 with tempfile.TemporaryDirectory(prefix='infozip-first-winner-') as td:
  base=Path(td)
  idx=0
  for gi,g in enumerate(groups,1):
   for order in itertools.permutations(g):
    idx+=1;dest=base/f'{idx:03d}';dest.mkdir()
    commands=[]
    for pid in order:
     cp=subprocess.run([unzip,'-n','-q',str(ids[pid]),'-d',str(dest)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
     # Info-ZIP may return 1 for warnings; actual extracted map is authoritative. Reject harder failures.
     commands.append({'provider':pid,'returncode':cp.returncode,'stderr':cp.stderr[-500:]})
     if cp.returncode>1:raise RuntimeError(f'unzip failed for {pid}: {cp.stderr}')
    actual=extracted_map(dest);exp=expected(order,maps)
    miss=sorted(set(exp)^set(actual));diff=sorted(n for n in set(exp)&set(actual) if exp[n]!=actual[n])
    rec={'group':gi,'order':list(order),'expected_sha256':mapdigest(exp),'actual_sha256':mapdigest(actual),
         'expected_entries':len(exp),'actual_entries':len(actual),'missing_or_extra_paths':miss,'different_byte_paths':diff,'commands':commands}
    rows.append(rec)
    if miss or diff:mismatches.append(rec)
 report={'schema_version':1,'engine':subprocess.check_output([unzip,'-v'],text=True,stderr=subprocess.STDOUT).splitlines()[0],
         'frame_archive_count':len(jars),'group_count':len(groups),'order_count':len(rows),'mismatch_count':len(mismatches),
         'orders':rows,'interpretation':'External sequential extraction validates concrete first-winner byte maps; it does not expand the formal scope.'}
 out=ns.output or root/'results'/'infozip-validation.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
 md=['# Info-ZIP external merger validation','',report['interpretation'],'',f"- Engine: `{report['engine']}`",f"- Groups: {len(groups)}",f"- Orders: {len(rows)}",f"- Mismatches: {len(mismatches)}"]
 out.with_suffix('.md').write_text('\n'.join(md)+'\n')
 if ns.strict and (len(jars)!=107 or len(groups)!=4 or len(rows)!=42 or mismatches):raise SystemExit('unexpected Info-ZIP validation result')
if __name__=='__main__':main()
