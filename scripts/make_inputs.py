"""Deterministic, outcome-independent synthetic coverage; no public-build claim."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')

def graph(owners, rows, before=()):
    return {'kind':'graph', 'owners': owners, 'before': [list(e) for e in before],
            'rows':[{'key': key, 'present': list(P), 'good': list(G)} for key, P, G in rows]}

def inventory(owners, entries, observed, before=(), relocations=None):
    relocations = relocations or [[] for _ in owners]
    return {'kind':'inventory', 'providers':[
        {'id':f'p{i}', 'owner': o, 'relocations': relocations[i],
         'entries':[{'name': key, 'payload': value.encode().hex()} for key, value in sorted(entries[i].items())]}
        for i,o in enumerate(owners)], 'before':[list(x) for x in before],
        'observed':[{'name':key, 'payload':value.encode().hex()} for key,value in sorted(observed.items())]}

def generated(family, n):
    owners = ['developer'] + [f'lib:L{i}' for i in range(1,n)]
    entries = [{'r/target.bin':'same'} for _ in range(n)]
    observed = {'r/target.bin':'same'}; before=[]; relocations=None
    if family == 'identical':
        pass
    elif family == 'observed-chain':
        for i in range(n-1):
            name=f's/probe{i:03}.bin'; entries[i][name]='accept'; entries[i+1][name]='reject'; observed[name]='accept'
    elif family == 'shared-owner':
        owners = ['lib:shared'] * n
    elif family == 'precedence-chain':
        before = [(i,i+1) for i in range(n-1)]
    elif family == 'disjunctive-roots':
        name='s/release.bin'; observed[name]='accept'
        for i in range(n): entries[i][name]='accept' if i<2 else 'reject'
    elif family == 'observation-cycle':
        for i in range(n):
            name=f's/probe{i:03}.bin'; entries[i][name]='accept'; entries[(i+1)%n][name]='reject'; observed[name]='accept'
    elif family == 'path-relocation':
        entries = [{f'origin{i}/target.bin':'same'} for i in range(n)]
        observed={'r/target.bin':'same'}; relocations=[[[f'origin{i}/','r/']] for i in range(n)]
    elif family == 'missing-payload':
        observed['r/target.bin']='absent'
    else:
        raise ValueError(family)
    return inventory(owners,entries,observed,before,relocations)

def fixtures():
    D, A, B='developer','lib:A','lib:B'
    cases=[
      ('developer-singleton',graph([D],[('r', [0],[0])])),
      ('library-singleton',graph([A],[('r',[0],[0])])),
      ('equal-bytes-distinct-owners',graph([D,A],[('r',[0,1],[0,1])])),
      ('equal-bytes-same-owner',graph([A,A],[('r',[0,1],[0,1])])),
      ('no-equal-payload',graph([D,A],[('r',[0,1],[])])),
      ('no-provider',graph([D],[('r',[],[])])),
      ('incompatible-observations',graph([D,A],[('x',[0,1],[0]),('y',[0,1],[1])])),
      ('precedence-cycle',graph([D,A],[('r',[0,1],[0,1])],[(0,1),(1,0)])),
      ('self-precedence',graph([D],[('r',[0],[0])],[(0,0)])),
      ('empty-region-set',graph([D,A],[])),
      ('unused-provider',graph([D,A,B],[('r',[0,1],[0,1])],[(2,0)])),
      ('cross-region-forcing',graph([D,A],[('r',[0,1],[0,1]),('s',[0,1],[0])])),
      ('or-not-and',graph([D,A,B],[('r',[0,1,2],[0,1,2]),('s',[0,1,2],[0,1])])),
      ('developer-precedence',graph([D,A],[('r',[0,1],[0,1])],[(0,1)])),
      ('same-owner-shadowed-provider',graph([A,A,D],[('r',[0,1,2],[0,1,2]),('s',[0,2],[0])],[(0,1)])),
      ('prefix-boundary',inventory([D,A],[{'a/x.bin':'x'},{'ab/x.bin':'y'}],{'q/x.bin':'x','ab/x.bin':'y'},relocations=[[["a/","q/"]],[]])),
      ('longest-prefix',inventory([D],[{'a/b/x.bin':'x'}],{'z/x.bin':'x'},relocations=[[["a/","q/"],["a/b/","z/"]]])),
      ('simultaneous-not-cascading',inventory([D],[{'a/x.bin':'x'}],{'b/x.bin':'x'},relocations=[[["a/","b/"],["b/","c/"]]])),
      ('noninjective-provider-rejected',inventory([D],[{'a/x.bin':'x','b/x.bin':'x'}],{'c/x.bin':'x'},relocations=[[["a/","c/"],["b/","c/"]]])),
      ('bytecode-relocation-rejected',inventory([A],[{'a/X.class':'x'}],{'b/X.class':'x'},relocations=[[["a/","b/"]]])),
    ]
    return cases

def main():
    families=['identical','observed-chain','shared-owner','precedence-chain','disjunctive-roots','observation-cycle','path-relocation','missing-payload']
    index=[]
    for fi, family in enumerate(families):
        for j, n in enumerate([2,3,5,8,16]):
            name=f'g{fi*5+j+1:03}'
            dump(ROOT/'inputs/generated'/f'{name}.json', generated(family,n))
            index.append({'case':name,'group':'generated','phenomenon':family,'providers':n,'path':f'inputs/generated/{name}.json','admission':'accepted'})
    for i,(name,data) in enumerate(fixtures(),1):
        case=f'f{i:03}'
        dump(ROOT/'inputs/fixtures'/f'{case}.json',data)
        index.append({'case':case,'group':'fixture','phenomenon':name,'providers':len(data.get('owners',data.get('providers',[]))), 'path':f'inputs/fixtures/{case}.json','admission':'rejected' if name.endswith('-rejected') else 'accepted'})
    dump(ROOT/'inputs/index.json',index)
    print(f'wrote {len(index)} cases: 40 generated + 20 boundary fixtures')
if __name__=='__main__': main()
