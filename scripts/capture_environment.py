#!/usr/bin/env python3
from pathlib import Path
import argparse,json,os,platform,shutil,subprocess,sys
TOOLS=['python','java','javac','ant','unzip','zip','pdflatex','bibtex','qpdf','pdfinfo']
def ver(x):
 p=shutil.which(x)
 if not p:return {'path':None,'returncode':127,'version':'not found'}
 for args in ([x,'--version'],[x,'-version'],[x,'-v']):
  cp=subprocess.run(args,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  if cp.stdout.strip():return {'path':p,'returncode':cp.returncode,'version':cp.stdout.strip()[:4000]}
 return {'path':p,'returncode':cp.returncode,'version':''}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--artifact',type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument('--output',type=Path);ns=ap.parse_args();root=ns.artifact.resolve()
 d={'schema_version':1,'platform':platform.platform(),'python':sys.version,'executable':sys.executable,'cpu_count':os.cpu_count(),'tools':{x:ver(x) for x in TOOLS},
    'note':'This records one successful environment; it is not a claim that versions are necessary or sufficient.'}
 out=ns.output or root/'docs'/'environment-capture.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
 md=['# Environment capture','',d['note'],'',f"- Platform: `{d['platform']}`",f"- Python: `{d['python'].splitlines()[0]}`",f"- CPUs visible: {d['cpu_count']}",'','| Tool | Path | Version first line |','|---|---|---|']
 for k,v in d['tools'].items():md.append(f"| {k} | `{v['path'] or 'not found'}` | `{v['version'].splitlines()[0] if v['version'] else ''}` |")
 out.with_suffix('.md').write_text('\n'.join(md)+'\n')
if __name__=='__main__':main()
