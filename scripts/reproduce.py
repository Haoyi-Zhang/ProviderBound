"""Bounded clean reproduction for theory checks, public builds, and pilots.

Run from any working directory. Result files are written under --output.  A
failure stops the command and no successful summary is emitted.  The public
stage uses at most four worker processes and only the bundled, licensed inputs.
"""
from pathlib import Path
import argparse, json, os, resource, subprocess, sys, time
ROOT=Path(__file__).resolve().parents[1]

def run():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',default='reproduced',help='relative to repository root unless absolute')
    p.add_argument('--java',action='store_true',help='also compile and run the two benign owned Java builds')
    p.add_argument('--skip-public',action='store_true',help='developer-only shortcut; omits the 80 public Ant builds')
    args=p.parse_args(); out=Path(args.output)
    if not out.is_absolute(): out=ROOT/out
    out.mkdir(parents=True,exist_ok=True)
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONHASHSEED='0',OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
    commands=[('generate',[sys.executable,'scripts/make_inputs.py'],180),
              ('public-inputs',[sys.executable,'scripts/verify_public_inputs.py'],180),
              ('unit',[sys.executable,'-m','unittest','discover','-s','tests','-p','test_*.py','-v'],180),
              ('oracle',[sys.executable,'tests/oracle.py',str(out)],180),
              ('campaign',[sys.executable,'scripts/campaign.py',str(out)],180)]
    if not args.skip_public:
        commands.append(('public',[sys.executable,'scripts/public_corpus.py','--output',str(out/'public'),'--workers','4'],900))
    commands.append(('scale',[sys.executable,'scripts/scale.py',str(out)],180))
    if args.java: commands.append(('java',[sys.executable,'scripts/java_pilot.py',str(out)],180))
    t=time.monotonic(); before=resource.getrusage(resource.RUSAGE_CHILDREN); records=[]
    for name,cmd,timeout in commands:
        start=time.monotonic()
        result=subprocess.run(cmd,cwd=ROOT,env=env,text=True,capture_output=True,timeout=timeout)
        (out/f'{name}.txt').write_text(result.stdout+result.stderr,encoding='utf-8')
        records.append({'command':name,'exit_code':result.returncode,'wall_seconds':time.monotonic()-start,'timeout_seconds':timeout})
        if result.returncode:
            print(result.stdout+result.stderr,file=sys.stderr)
            raise SystemExit(result.returncode)
        print(f'{name}: PASS', flush=True)
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    summary={'commands':records,'logical_reproduction':'all requested documented stages completed',
             'cpu_seconds_children':after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
             'wall_seconds':time.monotonic()-t,'child_peak_rss_kib':after.ru_maxrss,
             'maximum_workers':4 if not args.skip_public else 1,'java_requested':args.java,
             'public_requested':not args.skip_public,
             'scope':'Execution success, external two-order conformance, and finite regression evidence; not a universal implementation proof.'}
    (out/'reproduction_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__': run()
