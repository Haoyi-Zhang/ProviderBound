#!/usr/bin/env python3
"""Independent information-baseline analysis for the preserved public JAR frame.

This program intentionally does not import the production generator or checker.
It discovers the frozen 107-JAR frame, constructs the non-metadata collision
graph, enumerates every order of each 3/4-provider connected component, and
compares local byte-compatible candidates with winners feasible for the entire
output map.
"""
from __future__ import annotations
import argparse, hashlib, itertools, json, os, re, zipfile
from collections import defaultdict, deque
from pathlib import Path
from typing import Dict

META_PREFIX='META-INF/'

def canonical(name:str)->str:
    name=name.replace('\\','/')
    if name.startswith('/') or '\x00' in name: raise ValueError(name)
    parts=name.split('/')
    if any(x in ('','.','..') for x in parts): raise ValueError(name)
    return '/'.join(parts)

def read_jar(path:Path)->dict[str,bytes]:
    out={}
    with zipfile.ZipFile(path) as z:
        for zi in z.infolist():
            if zi.is_dir(): continue
            try:n=canonical(zi.filename)
            except ValueError: continue
            if n.upper().startswith(META_PREFIX): continue
            # Duplicate names inside one provider violate the provider-map abstraction.
            if n in out: raise ValueError(f'duplicate normalized entry in {path}: {n}')
            out[n]=z.read(zi)
    return out

def discover_frame(root:Path)->Path:
    cands=[]
    for d in [root]+[p for p in root.rglob('*') if p.is_dir()]:
        try:n=sum(1 for p in d.rglob('*.jar') if p.is_file())
        except OSError:continue
        if n==107:cands.append(d)
    if cands:return max(cands,key=lambda p:len(p.parts))
    raise RuntimeError('could not auto-discover a directory containing exactly 107 JARs; pass --frame explicitly')

def digest_map(m:dict[str,bytes])->str:
    h=hashlib.sha256()
    for k in sorted(m):
        kb=k.encode();h.update(len(kb).to_bytes(4,'big'));h.update(kb);h.update(len(m[k]).to_bytes(8,'big'));h.update(m[k])
    return h.hexdigest()

def merge(order:tuple[str,...],maps:dict[str,dict[str,bytes]]):
    out={};winner={}
    for p in order:
        for n,b in maps[p].items():
            if n not in out: out[n]=b;winner[n]=p
    return out,winner

def components(nodes,adj):
    seen=set();out=[]
    for n in nodes:
        if n in seen:continue
        q=[n];seen.add(n);c=[]
        while q:
            x=q.pop();c.append(x)
            for y in adj[x]:
                if y not in seen:seen.add(y);q.append(y)
        out.append(sorted(c))
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--artifact',type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument('--frame',type=Path);ap.add_argument('--output',type=Path);ap.add_argument('--strict',action='store_true');ns=ap.parse_args()
    root=ns.artifact.resolve();frame=ns.frame.resolve() if ns.frame else discover_frame(root/'inputs')
    jars=sorted(p for p in frame.rglob('*.jar') if p.is_file())
    if len(jars)!=107:raise RuntimeError(f'expected 107 JARs, got {len(jars)}')
    ids={p.relative_to(frame).as_posix():p for p in jars};maps={k:read_jar(p) for k,p in ids.items()}
    names={k:set(v) for k,v in maps.items()};adj={k:set() for k in ids};pair_collisions=[]
    keys=sorted(ids)
    for i,a in enumerate(keys):
        for b in keys[i+1:]:
            common=names[a]&names[b]
            if common:
                adj[a].add(b);adj[b].add(a);pair_collisions.append({'a':a,'b':b,'entry_count':len(common)})
    comps=components(keys,adj)
    selected=[c for c in comps if 3<=len(c)<=4]
    group_rows=[];total_orders=0;total_classes=0;over_regions=0;extra_associations=0
    equal_reversal_regions=set()
    for gi,c in enumerate(selected,1):
        orders=list(itertools.permutations(c));total_orders+=len(orders)
        classes=defaultdict(list);output_maps={};winners={}
        for order in orders:
            out,win=merge(order,maps);d=digest_map(out);classes[d].append(order);output_maps[d]=out;winners[order]=win
        total_classes+=len(classes)
        class_rows=[]
        for d,ords in sorted(classes.items()):
            out=output_maps[d];local_over=0;extra=0
            for n,b in out.items():
                local={p for p in c if maps[p].get(n)==b}
                exact={winners[o][n] for o in ords}
                if not exact<=local:raise AssertionError('exact winner outside local byte candidates')
                if exact!=local:
                    local_over+=1;extra+=len(local-exact)
                # Content-identical winner reversal inside one output class.
                if len(exact)>1:equal_reversal_regions.add((gi,d,n))
            over_regions+=local_over;extra_associations+=extra
            class_rows.append({'output_sha256':d,'order_count':len(ords),'orders':[list(o) for o in ords],
                               'entry_count':len(out),'local_overapprox_region_count':local_over,
                               'extra_local_provider_associations':extra})
        group_rows.append({'group':gi,'providers':c,'provider_count':len(c),'order_count':len(orders),
                           'output_class_count':len(classes),'classes':class_rows})
    report={'schema_version':1,'frame':frame.relative_to(root).as_posix() if frame.is_relative_to(root) else str(frame),
            'archive_count':len(jars),'unordered_pair_count':len(jars)*(len(jars)-1)//2,
            'collision_pair_count':len(pair_collisions),'component_sizes':sorted(len(c) for c in comps if len(c)>1),
            'selected_group_count':len(selected),'enumerated_order_count':total_orders,'output_class_count':total_classes,
            'local_overapprox_region_count':over_regions,'extra_local_provider_associations':extra_associations,
            'equal_output_class_ambiguous_region_count':len(equal_reversal_regions),'groups':group_rows,
            'interpretation':('Local byte-compatible candidates ignore the requirement that every entry share one global provider order. '
                              'Known-order attribution is not a fair competitor because it is given the hidden order.')}
    out=ns.output or root/'results'/'information-baselines.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    md=['# Information-baseline analysis','',report['interpretation'],'',
        f"- Frozen archives: {len(jars)}",f"- Unordered pairs: {report['unordered_pair_count']}",f"- Collision pairs: {len(pair_collisions)}",
        f"- Selected 3/4-provider connected components: {len(selected)}",f"- Enumerated orders: {total_orders}",f"- Observable output classes: {total_classes}",
        f"- Output-class regions where local candidates strictly over-approximate globally feasible winners: {over_regions}",
        f"- Extra local provider associations: {extra_associations}",f"- Regions ambiguous within an identical complete output class: {len(equal_reversal_regions)}",'',
        '| Group | Providers | Orders | Output classes | Locally over-approximated regions |','|---:|---:|---:|---:|---:|']
    for g in group_rows:md.append(f"| {g['group']} | {g['provider_count']} | {g['order_count']} | {g['output_class_count']} | {sum(x['local_overapprox_region_count'] for x in g['classes'])} |")
    out.with_suffix('.md').write_text('\n'.join(md)+'\n')
    expected={'archive_count':107,'unordered_pair_count':5671,'collision_pair_count':40,'selected_group_count':4,'enumerated_order_count':42,'output_class_count':14,'local_overapprox_region_count':100}
    bad={k:(report[k],v) for k,v in expected.items() if report[k]!=v}
    if ns.strict and bad:raise SystemExit('unexpected retained-frame result: '+repr(bad))
if __name__=='__main__':main()
