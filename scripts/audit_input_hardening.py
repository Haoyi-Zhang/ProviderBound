#!/usr/bin/env python3
"""Static inventory of fail-closed input checks and adversarial test coverage."""
from pathlib import Path
import argparse,ast,json,re
TOKENS={
 'unknown_fields':[r'unknown field',r'unexpected field',r'extra field'],
 'duplicate_json_keys':[r'duplicate.*key',r'object_pairs_hook'],
 'schema_version':[r'schema.?version',r'unsupported.*version'],
 'path_traversal':[r'\.\.',r'path traversal',r'canonical path'],
 'absolute_paths':[r'absolute path',r'startswith\(.?/'],
 'backslashes':[r'backslash',r"'\\\\'"],
 'nul':[r'nul',r'\\x00'],
 'noncanonical_hex':[r'canonical.*hex',r'lowercase.*hex'],
 'malformed_order':[r'order.*constraint',r'cycle'],
 'unsupported_transform':[r'unsupported.*transform',r'relocation'],
}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--artifact',type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument('--output',type=Path);ns=ap.parse_args();root=ns.artifact.resolve()
 py=[]
 for p in root.rglob('*.py'):
  if '__pycache__' not in p.parts:
   try:txt=p.read_text(encoding='utf-8')
   except:continue
   py.append((p,txt))
 corpus='\n'.join(t.lower() for _,t in py)
 coverage={k:{'present':any(re.search(p,corpus,re.I) for p in pats),'patterns':pats} for k,pats in TOKENS.items()}
 raw=[]
 for p,t in py:
  for no,line in enumerate(t.splitlines(),1):
   if re.search(r'json\.(?:load|loads)\s*\(',line) and not re.search(r'(dump|dumps)',line):
    raw.append({'file':p.relative_to(root).as_posix(),'line':no,'text':line.strip(),
                'strict_hook_on_line':bool(re.search(r'object_pairs_hook|parse_constant',line))})
 report={'schema_version':1,'coverage_inventory':coverage,'raw_json_load_sites':raw,
         'note':'Presence is a static navigation aid, not proof that every path is hardened. Runtime adversarial tests remain authoritative.'}
 out=ns.output or root/'docs'/'input-hardening-audit.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
 md=['# Input-hardening audit','',report['note'],'','| Concern | Source/test evidence present |','|---|---|']+[f"| {k.replace('_',' ')} | {'yes' if v['present'] else 'no'} |" for k,v in coverage.items()]
 md += ['','## Raw JSON-load sites','', '| Source | Strict hook visible on call line | Code |','|---|---|---|']+[f"| `{x['file']}:{x['line']}` | {'yes' if x['strict_hook_on_line'] else 'no / wrapper inspection required'} | `{x['text'].replace('|','\\|')}` |" for x in raw]
 out.with_suffix('.md').write_text('\n'.join(md)+'\n')
if __name__=='__main__':main()
