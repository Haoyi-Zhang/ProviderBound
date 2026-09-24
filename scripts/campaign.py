"""Replay the fixed 40 generated cases and 20 fixtures; not a public-build study."""
from pathlib import Path
import csv, json, sys, time, resource
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
from producer import infer, normalize, InputError
from checker import verify, Rejected, read_model
ROOT=Path(__file__).resolve().parents[1]

def run(output):
    output=Path(output); (output/'certificates').mkdir(parents=True,exist_ok=True)
    index=json.loads((ROOT/'inputs/index.json').read_text()); records=[]
    t0=time.process_time(); wall=time.monotonic()
    for item in index:
        raw=json.loads((ROOT/item['path']).read_text()); t=time.process_time()
        try:
            model=normalize(raw); cert=infer(raw)
        except (InputError,ValueError,TypeError,KeyError) as exc:
            assert item['admission']=='rejected', (item,exc)
            try: read_model(raw)
            except (Rejected,ValueError,TypeError,KeyError): pass
            else: raise AssertionError('checker admitted unsupported input')
            records.append(dict(case=item['case'], group=item['group'],phenomenon=item['phenomenon'],providers=item['providers'],
                                rows=0,incidences=0,status='admission-rejected',developer=0,library=0,ambiguous=0,
                                dependency_strictly_narrowed=0,bytes_strictly_narrowed=0,orders=0,certificate_bytes=0,
                                producer_cpu_seconds=0,checker_cpu_seconds=0)); continue
        produced=time.process_time()-t; t=time.process_time()
        answer=verify(raw,cert); checked=time.process_time()-t
        assert item['admission']=='accepted'
        text=json.dumps(cert,sort_keys=True,separators=(',',':'))+'\n'
        (output/'certificates'/f"{item['case']}.json").write_text(text)
        count={k:0 for k in ('developer','library','ambiguous')}; dep=byte=0
        if answer['status']=='classified':
            for row, region in zip(model['rows'],answer['regions']):
                count[region['class']]+=1
                exact=set(region['owners'])
                local_bytes={model['owners'][p] for p in row['good']}
                local_dep={model['owners'][p] for p in row['present']}
                assert exact <= local_bytes <= local_dep
                byte+=exact<local_bytes; dep+=exact<local_dep
        records.append(dict(case=item['case'],group=item['group'],phenomenon=item['phenomenon'],providers=len(model['owners']),
                            rows=len(model['rows']),incidences=len(model['before'])+sum(len(r['present']) for r in model['rows']),
                            status=answer['status'],**count,dependency_strictly_narrowed=dep,bytes_strictly_narrowed=byte,
                            orders=len(cert.get('orders',[])),certificate_bytes=len(text.encode()),
                            producer_cpu_seconds=produced,checker_cpu_seconds=checked))
    with (output/'cases.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(records[0])); writer.writeheader(); writer.writerows(records)
    summary={'cases':len(records),'generated_cases':40,'boundary_fixtures':20,'public_builds':0,
             'classified_inputs':sum(x['status']=='classified' for x in records),
             'inconsistent_inputs':sum(x['status']=='inconsistent' for x in records),
             'admission_rejected_inputs':sum(x['status']=='admission-rejected' for x in records),
             **{key:sum(x[key] for x in records) for key in ('rows','incidences','developer','library','ambiguous','dependency_strictly_narrowed','bytes_strictly_narrowed','certificate_bytes')},
             'cpu_seconds':time.process_time()-t0,'wall_seconds':time.monotonic()-wall,
             'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
             'baseline_scope':'Local provider membership and exact-byte owner sets only; no whitelist or package-frequency tool evaluation.'}
    (output/'campaign_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    return summary
if __name__=='__main__': print(json.dumps(run(sys.argv[1] if len(sys.argv)>1 else ROOT/'results'),indent=2))
