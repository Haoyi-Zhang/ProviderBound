"""Fixed synthetic representation probes. No worst-case or Android-build claim."""
from pathlib import Path
import json, time, sys, tempfile
from telemetry import usage
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from producer import infer
from checker import verify, load as load_certificate
ROOT=Path(__file__).resolve().parents[1]

def make_case(name):
    n=300; owners=['developer']+[f'lib:{p}' for p in range(1,n)]
    if name=='repeated-collision':
        rows=[{'key':f'r{i:05}','present':list(range(12)),'good':list(range(12))} for i in range(20000)]; edges=[]
    elif name=='forced-repeated-collision':
        rows=[{'key':f'r{i:05}','present':list(range(12)),'good':list(range(12))} for i in range(19989)]
        rows += [{'key':f's{i:05}','present':[i,i+1],'good':[i]} for i in range(11)]; edges=[]
    elif name=='distributed-collision':
        rows=[{'key':f'r{i:05}','present':[(i+j)%300 for j in range(3)],'good':[(i+j)%300 for j in range(3)]} for i in range(900)]; edges=[]
    else: raise ValueError(name)
    return {'kind':'graph','owners':owners,'before':edges,'rows':rows}

def run(output):
    output=Path(output); output.mkdir(parents=True,exist_ok=True); records=[]
    for name in ('repeated-collision','forced-repeated-collision','distributed-collision'):
        case=make_case(name); t=time.process_time(); wall=time.monotonic(); cert=infer(case); produced=time.process_time()-t
        encoded=json.dumps(cert,separators=(',',':'))
        # Exercise the documented disk parser, not merely the in-memory API.
        with tempfile.TemporaryDirectory(prefix='boundary-scale-') as folder:
            path=Path(folder)/'certificate.json'; path.write_text(encoded)
            t=time.process_time(); result=verify(case,load_certificate(path)); checked=time.process_time()-t
        assert result['status']=='classified'
        expected=12 if name=='repeated-collision' else 1 if name=='forced-repeated-collision' else 3
        assert all(len(x['owners'])==expected for x in result['regions'])
        records.append({'case':name,'providers':300,'regions':len(case['rows']),
          'incidences':sum(len(r['present']) for r in case['rows']),
          'orders':len(cert['orders']),'certificate_bytes':len(encoded.encode()),'obstructions':len(cert['obstructions']),
          'producer_cpu_seconds':produced,'checker_cpu_seconds':checked,'wall_seconds':time.monotonic()-wall,
          'peak_rss_kib':usage()['peak_rss_kib'], 'rss_scope':usage()['scope']})
    (output/'scale_summary.json').write_text(json.dumps(records,indent=2)+'\n')
    return records
if __name__=='__main__': print(json.dumps(run(sys.argv[1] if len(sys.argv)>1 else ROOT/'results'),indent=2))
