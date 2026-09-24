#!/usr/bin/env python3
"""One-command reproduction and artifact-only release audit.

The command works from the standalone artifact ZIP; it does not require the
paper directory or network access.  Timing fields are descriptive and are not
used as pass/fail criteria.
"""
from __future__ import annotations
import argparse, hashlib, json, os, subprocess, sys, time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def run(cmd, cwd=ROOT, timeout=1800):
    start=time.perf_counter()
    p=subprocess.run(cmd,cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=timeout)
    elapsed=time.perf_counter()-start
    if p.returncode:
        raise SystemExit(f"FAILED ({p.returncode}): {' '.join(map(str,cmd))}\n"+'\n'.join(p.stdout.splitlines()[-120:]))
    return {'command':[str(x) for x in cmd],'seconds':elapsed,'output_tail':p.stdout.splitlines()[-20:]}

def sha256(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()

def verify_manifest():
    path=ROOT/'RELEASE-MANIFEST.sha256'
    if not path.exists(): return {'present':False,'checked':0,'mismatches':[]}
    mismatches=[]; checked=0
    for line in path.read_text(encoding='utf-8').splitlines():
        if not line.strip(): continue
        digest,rel=line.split('  ',1); p=ROOT/rel
        checked+=1
        if not p.is_file(): mismatches.append({'path':rel,'reason':'missing'})
        elif sha256(p)!=digest: mismatches.append({'path':rel,'reason':'sha256'})
    return {'present':True,'checked':checked,'mismatches':mismatches}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--java',action='store_true')
    args=ap.parse_args()
    manifest=verify_manifest()
    if manifest['present'] and manifest['mismatches']:
        raise SystemExit(f"Release manifest mismatch: {manifest['mismatches'][:10]}")
    out=args.output.resolve(); out.mkdir(parents=True,exist_ok=True)
    records=[]
    cmd=[sys.executable,'scripts/reproduce.py','--output',str(out/'core')]
    if args.java: cmd.append('--java')
    records.append(run(cmd))
    steps=[
      [sys.executable,'scripts/analyze_information_baselines.py'],
      [sys.executable,'scripts/validate_infozip_merger.py'],
      [sys.executable,'scripts/analyze_metadata_sensitivity.py'],
      [sys.executable,'scripts/analyze_certificate_compression.py'],
      [sys.executable,'scripts/audit_claims.py'],
      [sys.executable,'scripts/audit_archive_safety.py','--strict'],
      [sys.executable,'scripts/audit_independence.py','--strict'],
      [sys.executable,'scripts/audit_security_test_evidence.py','--strict'],
      [sys.executable,'scripts/audit_input_hardening.py'],
      [sys.executable,'scripts/inventory_third_party.py'],
      [sys.executable,'scripts/build_data_dictionary.py'],
      [sys.executable,'scripts/audit_source_quality.py'],
    ]
    for step in steps: records.append(run(step))
    result={
      'schema_version':1,'status':'PASS','artifact_root':str(ROOT),
      'manifest_verification':manifest,'java_enabled':args.java,
      'steps':records,'wall_seconds':sum(r['seconds'] for r in records),
      'timing_note':'Times are descriptive observations for this run, not portable bounds.'
    }
    (out/'release-reproduction.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    md=['# Release Reproduction','', '**Status: PASS**','',f"Manifest files checked: **{manifest['checked']}**",f"Java integration enabled: **{args.java}**",f"Summed step wall time: **{result['wall_seconds']:.3f} s**",'',result['timing_note'],'','## Steps','']
    md += [f"- PASS — `{' '.join(r['command'])}` ({r['seconds']:.3f} s)" for r in records]
    (out/'release-reproduction.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','output':str(out),'steps':len(records)},sort_keys=True))
if __name__=='__main__': main()
