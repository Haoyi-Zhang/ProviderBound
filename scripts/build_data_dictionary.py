#!/usr/bin/env python3
from pathlib import Path
import argparse,csv,json

def shape(v):
 if isinstance(v,dict): return 'object',len(v)
 if isinstance(v,list): return 'array',len(v)
 if v is None:return 'null',''
 return type(v).__name__,''

def walk(v,p=''):
 t,n=shape(v); yield p or '/',t,n
 if isinstance(v,dict):
  for k,x in v.items(): yield from walk(x,p+'/'+str(k).replace('~','~0').replace('/','~1'))
 elif isinstance(v,list) and v:
  # Schema-oriented sample plus homogeneity count.
  yield from walk(v[0],p+'/0')

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--artifact',type=Path,default=Path(__file__).resolve().parents[1]);ns=ap.parse_args();root=ns.artifact.resolve()
 rows=[]
 for p in sorted(root.rglob('*')):
  if not p.is_file() or any(x in p.parts for x in ('__pycache__','reproduced')):continue
  rel=p.relative_to(root).as_posix()
  if p.suffix.lower()=='.json':
   try:o=json.loads(p.read_text(encoding='utf-8'))
   except:continue
   for ptr,t,n in walk(o):rows.append({'file':rel,'location':ptr,'type':t,'extent':n})
  elif p.suffix.lower()=='.csv':
   try:
    with p.open(newline='',encoding='utf-8') as f:
     rd=csv.reader(f); hdr=next(rd); count=sum(1 for _ in rd)
    for h in hdr:rows.append({'file':rel,'location':h,'type':'CSV column','extent':count})
   except:continue
 out=root/'docs'/'data-dictionary.json';out.write_text(json.dumps({'schema_version':1,'fields':rows},indent=2,sort_keys=True)+'\n')
 md=['# Data dictionary','', 'JSON locations use RFC 6901-style pointers. For arrays, the first element documents the retained schema; `extent` records array or CSV row counts.','',
     '| File | Location | Type | Extent |','|---|---|---|---:|']
 md += [f"| `{r['file']}` | `{r['location']}` | {r['type']} | {r['extent']} |" for r in rows]
 (root/'docs'/'data-dictionary.md').write_text('\n'.join(md)+'\n')
if __name__=='__main__':main()
