"""Independent literal enumeration of total provider orders. Bound: <=3 providers.

This is finite evidence, not mechanized universal proof. A graph row has one of
three states for each provider (absent, wrong bytes, equal bytes), except that the
all-absent row is covered separately by a boundary fixture. Every off-diagonal
precedence relation, including cyclic ones, is included.
"""
from itertools import product, permutations
from pathlib import Path
import csv, json, time, sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from telemetry import usage
from producer import infer
from checker import verify

ROOT=Path(__file__).resolve().parents[1]

def worlds(n, rows, edges):
    result=[]
    for order in permutations(range(n)):
        rank={p:i for i,p in enumerate(order)}
        if any(rank[a]>=rank[b] for a,b in edges): continue
        first=[]; ok=True
        for row in rows:
            chosen=next(p for p in order if p in row['present'])
            if chosen not in row['good']: ok=False; break
            first.append(chosen)
        if ok: result.append(first)
    return result

def run(output):
    t=time.process_time(); wall=time.monotonic(); total=feasible=classified_regions=0; records=[]
    for n in (1,2,3):
        rowtypes=[]
        for flags in product(range(3),repeat=n):
            P=[i for i,f in enumerate(flags) if f]; G=[i for i,f in enumerate(flags) if f==2]
            if P: rowtypes.append((P,G))
        all_edges=[(i,j) for i in range(n) for j in range(n) if i!=j]
        for mask in range(1<<len(all_edges)):
            E=[list(edge) for k,edge in enumerate(all_edges) if mask>>k&1]
            count=ok_count=0
            for m in (0,1,2):
                for combination in product(rowtypes,repeat=m):
                    rows=[{'key':f'r{r}','present':P,'good':G} for r,(P,G) in enumerate(combination)]
                    admissible=worlds(n,rows,E)
                    for scheme in ('distinct','shared'):
                        owners=(['developer']+[f'lib:{i}' for i in range(1,n)]) if scheme=='distinct' else ['lib:shared']*n
                        raw={'kind':'graph','owners':owners,'before':E,'rows':rows}
                        cert=infer(raw); checked=verify(raw,cert)
                        assert (checked['status']=='classified') == bool(admissible), (raw,cert,admissible)
                        if admissible:
                            for r in range(m):
                                expected=sorted({owners[w[r]] for w in admissible})
                                assert checked['regions'][r]['owners']==expected,(raw,cert,expected)
                            ok_count+=1; classified_regions+=m
                        count+=1
            records.append({'providers':n,'precedence_mask':mask,'structures':count//2,'labelled_cases':count,'feasible_labelled_cases':ok_count})
            total+=count; feasible+=ok_count
    output=Path(output); output.mkdir(parents=True,exist_ok=True)
    with (output/'oracle_details.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(records[0])); w.writeheader(); w.writerows(records)
    summary={'structural_cases':total//2,'labelled_cases':total,'feasible_labelled_cases':feasible,
             'region_classifications_checked':classified_regions,'mismatches':0,
             'provider_counts':[1,2,3],'region_counts':[0,1,2],
             'owner_schemes':['one distinct owner per provider; provider zero is developer','all providers belong to the same named library'],
             'cpu_seconds':time.process_time()-t,'wall_seconds':time.monotonic()-wall,
             'peak_rss_kib':usage()['peak_rss_kib'], 'rss_scope':usage()['scope']}
    (output/'oracle_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    return summary
if __name__=='__main__':
    print(json.dumps(run(sys.argv[1] if len(sys.argv)>1 else ROOT/'results'),indent=2))
