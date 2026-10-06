#!/usr/bin/env python3
"""Build and exhaustively check the bundled public two-provider archive corpus.

All 40 public-provider pairs with a non-META-INF collision are assembled by
Apache Ant in both orders.  The 80 concrete builds enumerate the complete order
space for each pair and therefore act as an external exact oracle.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, os, statistics, subprocess, sys, time
from telemetry import usage
from collections import Counter
from concurrent.futures import ProcessPoolExecutor, as_completed
from html import escape
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from archive_producer import lower_archives, read_archive
from archive_checker import interpret_archives
from producer import infer
from checker import verify, load as load_certificate


def _digest(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''): h.update(block)
    return h.hexdigest()

def _read_csv(path: Path):
    with path.open(newline='', encoding='utf-8') as f: return list(csv.DictReader(f))

def _write_csv(path: Path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='', encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

def _ant_xml(pairs, jars: Path, out: Path):
    lines=['<project default="all">','  <target name="all">']
    for r in pairs:
        a=jars/r['left']; b=jars/r['right']
        for suffix,seq in (('ab',(a,b)),('ba',(b,a))):
            target=out/f"{r['pair_id']}-{suffix}.zip"
            lines.append(f'    <zip destfile="{escape(str(target),quote=True)}" duplicate="preserve" filesonly="true">')
            for source in seq:
                lines.append(f'      <zipfileset src="{escape(str(source),quote=True)}" excludes="META-INF/MANIFEST.MF" defaultexcludes="no"/>')
            lines.append('    </zip>')
    lines += ['  </target>','</project>']
    return '\n'.join(lines)+'\n'

def _expected(first,second):
    answer=dict(second); answer.update(first); return answer

def certificate_sizes(sizes):
    return {'certificate_bytes_min':min(sizes),
            'certificate_bytes_median':statistics.median(sizes),
            'certificate_bytes_max':max(sizes)}

def _process_pair(args):
    record, jars_text, outputs_text, retained_text = args
    jars=Path(jars_text); outputs=Path(outputs_text); retained=Path(retained_text)
    pair=record['pair_id']; left_path=jars/record['left']; right_path=jars/record['right']
    left_owner=f"lib:{record['left'][:-4]}"; right_owner=f"lib:{record['right'][:-4]}"
    provider_maps=[read_archive(left_path),read_archive(right_path)]
    output_paths=[outputs/f'{pair}-ab.zip',outputs/f'{pair}-ba.zip']
    output_maps=[read_archive(p) for p in output_paths]
    equal_outputs=output_maps[0]==output_maps[1]
    flips=sum(1 for k in set(provider_maps[0]) & set(provider_maps[1])) if equal_outputs else 0
    rows=[]; aggregate=Counter(); cert_sizes=[]
    kept={"p001-ab","p021-ab","p039-ab"}
    for number,(suffix,order) in enumerate((('ab',[0,1]),('ba',[1,0]))):
        build_id=f'{pair}-{suffix}'; output_path=output_paths[number]
        ant_exact=_expected(provider_maps[order[0]],provider_maps[order[1]])==output_maps[number]
        specs=[('left',left_owner,left_path),('right',right_owner,right_path)]
        checker_specs=[{'id':'left','owner':left_owner,'path':str(left_path)},
                       {'id':'right','owner':right_owner,'path':str(right_path)}]
        t=time.perf_counter(); graph=lower_archives(specs,output_path); t_lower=time.perf_counter()-t
        graph2=interpret_archives(checker_specs,output_path); adapters_equal=graph==graph2
        t=time.perf_counter(); cert=infer(graph); t_infer=time.perf_counter()-t
        encoded=json.dumps(cert,separators=(',',':'),sort_keys=True).encode()
        certificate_path=outputs/f'{build_id}.certificate.json'
        certificate_path.write_bytes(encoded)
        t=time.perf_counter(); answer=verify(graph2,load_certificate(certificate_path)); t_check=time.perf_counter()-t
        cert_sizes.append(len(encoded))
        admissible=[candidate for candidate,actual in zip(([0,1],[1,0]),output_maps) if actual==output_maps[number]]
        by_key={x['key']:x for x in answer['regions']}
        mismatch=narrow=local_amb=cert_amb=collisions=coupled=0
        baseline={name:Counter() for name in ('catalogue_tiebreak','inventory_size_proxy','dependency','local_bytes','certified','trusted_trace')}
        for row in graph['rows']:
            present=row['present']; key=row['key']
            if len(present)>1: collisions+=1
            actual_owners=set()
            for actual_order in admissible:
                for p in actual_order:
                    if p in present:
                        actual_owners.add((left_owner,right_owner)[p]); break
            model=set(by_key[key]['owners'])
            if model!=actual_owners: mismatch+=1
            local={(left_owner,right_owner)[p] for p in row['good']}
            local_amb += len(local)>1; cert_amb += len(model)>1
            if len(present)>1:
                hidden={(left_owner,right_owner)[order[0]]}
                # Information-limited baselines: a fixed catalogue tie-break and
                # a provider-inventory-size proxy.  These are deliberately not
                # presented as reimplementations of any published detector.
                catalogue={left_owner}
                left_size=len(provider_maps[0]); right_size=len(provider_maps[1])
                size_proxy={left_owner if left_size>=right_size else right_owner}
                methods={
                    'catalogue_tiebreak':catalogue, 'inventory_size_proxy':size_proxy,
                    'dependency':{(left_owner,right_owner)[p] for p in present},
                    'local_bytes':local, 'certified':model, 'trusted_trace':hidden}
                for method,estimate in methods.items():
                    baseline[method]['observations'] += 1
                    baseline[method]['set_size'] += len(estimate)
                    baseline[method]['oracle_exact'] += estimate == actual_owners
                    baseline[method]['oracle_conservative'] += actual_owners <= estimate
                    baseline[method]['hidden_winner_covered'] += bool(hidden <= estimate)
            if model < local:
                narrow += 1
                if len(present)==2 and len(row['good'])==2: coupled += 1
        aggregate.update({
            'regions':len(graph['rows']),'collisions':collisions,'local_amb':local_amb,
            'cert_amb':cert_amb,'narrow':narrow,'coupled':coupled,'oracle_mismatch':mismatch,
            'ant_mismatch':0 if ant_exact else 1,'adapter_mismatch':0 if adapters_equal else 1})
        for method,metrics in baseline.items():
            for metric,value in metrics.items(): aggregate[f'baseline.{method}.{metric}'] += value
        if build_id in kept:
            retained.mkdir(parents=True,exist_ok=True)
            (retained/f'{build_id}.graph.json').write_text(json.dumps(graph,indent=2)+'\n')
            (retained/f'{build_id}.certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
            (retained/f'{build_id}.answer.json').write_text(json.dumps(answer,indent=2)+'\n')
        rows.append({
            'build_id':build_id,'pair_id':pair,'pair_kind':record['kind'],
            'first_archive':record['left'] if suffix=='ab' else record['right'],
            'second_archive':record['right'] if suffix=='ab' else record['left'],
            'entry_regions':len(graph['rows']),'collision_regions':collisions,
            'admissible_actual_orders':len(admissible),'ant_matches_first_winner':int(ant_exact),
            'archive_adapters_equal':int(adapters_equal),'oracle_mismatches':mismatch,
            'local_ambiguous_regions':local_amb,'certified_ambiguous_regions':cert_amb,
            'global_narrowings':narrow,'equal_regions_resolved_by_coupling':coupled,
            'witness_orders':len(cert.get('orders',[])),'obstructions':len(cert.get('obstructions',[])),
            'certificate_bytes':len(encoded),'output_bytes':output_path.stat().st_size,
            'output_sha256':_digest(output_path),
            'catalogue_tiebreak_oracle_exact':baseline['catalogue_tiebreak']['oracle_exact'],
            'inventory_size_proxy_oracle_exact':baseline['inventory_size_proxy']['oracle_exact'],
            'dependency_oracle_exact':baseline['dependency']['oracle_exact'],
            'local_bytes_oracle_exact':baseline['local_bytes']['oracle_exact'],
            'certified_oracle_exact':baseline['certified']['oracle_exact'],
            'trusted_trace_hidden_winner_covered':baseline['trusted_trace']['hidden_winner_covered'],
            'lowering_seconds':f'{t_lower:.6f}','inference_seconds':f'{t_infer:.6f}','checking_seconds':f'{t_check:.6f}'})
    return {'rows':rows,'counts':dict(aggregate),'equal_outputs':equal_outputs,'flips':flips,'cert_sizes':cert_sizes}

def run(destination: Path, workers: int=4, prebuilt: Path|None=None):
    destination.mkdir(parents=True,exist_ok=True)
    public=ROOT/'inputs/public'; jars=public/'jars'; pairs=_read_csv(public/'collision_pairs.csv')
    if len(pairs)!=40: raise RuntimeError(f'frozen corpus expected 40 pairs, found {len(pairs)}')
    workers=max(1,min(4,workers))
    usage0=usage(children=True); wall=time.perf_counter(); cpu=time.process_time()
    temp=None
    try:
        if prebuilt is None:
            temp=TemporaryDirectory(prefix='boundary-public-', dir=str(destination.parent)); work=Path(temp.name); outputs=work/'outputs'; outputs.mkdir()
            build=work/'build.xml'; build.write_text(_ant_xml(pairs,jars,outputs))
            cp=os.pathsep.join((str(jars/'ant-1.10.15.jar'),str(jars/'ant-launcher-1.10.15.jar')))
            command=['java','-Xmx768m','-cp',cp,'org.apache.tools.ant.Main','-q','-f',str(build)]
            result=subprocess.run(command,text=True,capture_output=True,timeout=900)
            (destination/'builder.log').write_text(result.stdout+result.stderr)
            if result.returncode: raise RuntimeError(f'Apache Ant failed: {result.returncode}')
        else:
            outputs=prebuilt
            (destination/'builder.log').write_text('Reused previously generated Apache Ant outputs for this run.\n')
        missing=[f"{r['pair_id']}-{s}.zip" for r in pairs for s in ('ab','ba') if not (outputs/f"{r['pair_id']}-{s}.zip").is_file()]
        if missing: raise RuntimeError('missing build outputs: '+','.join(missing[:3]))
        retained=destination/'retained'; retained.mkdir(exist_ok=True)
        payload=[(r,str(jars),str(outputs),str(retained)) for r in pairs]
        results=[]
        with ProcessPoolExecutor(max_workers=workers) as pool:
            futures=[pool.submit(_process_pair,x) for x in payload]
            for f in as_completed(futures): results.append(f.result())
        rows=sorted((row for result in results for row in result['rows']),key=lambda x:x['build_id'])
        counts=Counter(); cert_sizes=[]
        for result in results:
            counts.update(result['counts']); cert_sizes.extend(result['cert_sizes'])
        categories=Counter(r['kind'] for r in pairs)
        baseline_summary={}
        for method in ('catalogue_tiebreak','inventory_size_proxy','dependency','local_bytes','certified','trusted_trace'):
            n=counts[f'baseline.{method}.observations']
            baseline_summary[method]={
                'observations':n,
                'oracle_exact_count':counts[f'baseline.{method}.oracle_exact'],
                'oracle_exact_rate':round(counts[f'baseline.{method}.oracle_exact']/n,6),
                'oracle_conservative_rate':round(counts[f'baseline.{method}.oracle_conservative']/n,6),
                'hidden_winner_coverage_rate':round(counts[f'baseline.{method}.hidden_winner_covered']/n,6),
                'mean_owner_set_size':round(counts[f'baseline.{method}.set_size']/n,6)}
        usage1=usage(children=True)
        summary={
            'public_provider_archives':43,'collision_pairs':40,'actual_ant_builds':80,
            'pair_categories':dict(sorted(categories.items())),
            'reversed_pairs_with_identical_output_maps':sum(r['equal_outputs'] for r in results),
            'indistinguishable_shared_regions_with_owner_flip':sum(r['flips'] for r in results),
            'region_observations':counts['regions'],'collision_region_observations':counts['collisions'],
            'local_byte_ambiguous_regions':counts['local_amb'],'certified_ambiguous_regions':counts['cert_amb'],
            'global_narrowings_over_local_bytes':counts['narrow'],
            'equal_byte_regions_resolved_by_global_coupling':counts['coupled'],
            'ant_first_winner_mismatches':counts['ant_mismatch'],
            'independent_archive_adapter_mismatches':counts['adapter_mismatch'],
            'certificate_vs_actual_two_order_oracle_mismatches':counts['oracle_mismatch'],
            'baseline_comparison_on_collision_regions':baseline_summary,
            **certificate_sizes(cert_sizes),'elapsed_seconds':round(time.perf_counter()-wall,6),
            'process_cpu_seconds':round(time.process_time()-cpu,6),
            'child_cpu_seconds':None if usage1['cpu_seconds'] is None else round(usage1['cpu_seconds']-usage0['cpu_seconds'],6),
            'child_peak_rss_kib':usage1['peak_rss_kib'],'rss_scope':usage1['scope'],'workers':workers,
            'builder':'Apache Ant 1.10.15 Zip task, duplicate=preserve, filesonly=true',
            'manifest_handling':'META-INF/MANIFEST.MF excluded from providers and outputs',
            'oracle_scope':'For each two-provider pair, concrete builds in both orders enumerate all total orders.'}
        if counts['ant_mismatch'] or counts['adapter_mismatch'] or counts['oracle_mismatch']:
            raise RuntimeError('public-corpus conformance mismatch')
        _write_csv(destination/'cases.csv',rows)
        (destination/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
        (destination/'summary.txt').write_text('\n'.join(f'{k}: {v}' for k,v in summary.items())+'\n')
        return summary
    finally:
        if temp is not None: temp.cleanup()

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,default=ROOT/'results/public')
    p.add_argument('--workers',type=int,default=4)
    p.add_argument('--prebuilt-output-dir',type=Path)
    a=p.parse_args()
    try: print(json.dumps(run(a.output,a.workers,a.prebuilt_output_dir),indent=2))
    except (OSError,ValueError,RuntimeError,subprocess.TimeoutExpired) as exc: p.exit(2,f'public corpus failed: {exc}\n')
if __name__=='__main__': main()
