#!/usr/bin/env python3
from pathlib import Path
import argparse,ast,json,re

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--artifact',type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument('--output',type=Path);ns=ap.parse_args();root=ns.artifact.resolve()
 files=[];findings=[];tests=0;functions=0;lines=0
 for p in sorted(root.rglob('*.py')):
  if '__pycache__' in p.parts:continue
  text=p.read_text(encoding='utf-8');lines+=len(text.splitlines());tree=ast.parse(text,filename=str(p));rel=p.relative_to(root).as_posix()
  tf=0
  for n in ast.walk(tree):
   if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)):
    functions+=1
    if n.name.startswith('test_'):tests+=1;tf+=1
   if isinstance(n,ast.ExceptHandler) and n.type is None:findings.append({'kind':'bare-except','file':rel,'line':n.lineno})
   if isinstance(n,ast.Call):
    name=''
    if isinstance(n.func,ast.Name):name=n.func.id
    elif isinstance(n.func,ast.Attribute):name=n.func.attr
    if name in {'eval','exec'}:findings.append({'kind':name,'file':rel,'line':n.lineno})
    if name in {'loads','load'} and isinstance(n.func,ast.Attribute) and isinstance(n.func.value,ast.Name) and n.func.value.id=='pickle':findings.append({'kind':'pickle-load','file':rel,'line':n.lineno})
    if name in {'run','Popen','call','check_output','check_call'}:
     for kw in n.keywords:
      if kw.arg=='shell' and isinstance(kw.value,ast.Constant) and kw.value.value is True:findings.append({'kind':'subprocess-shell-true','file':rel,'line':n.lineno})
  for no,line in enumerate(text.splitlines(),1):
   if re.search(r'\b(TODO|FIXME|XXX)\b',line,re.I):findings.append({'kind':'unfinished-marker','file':rel,'line':no,'text':line.strip()})
  files.append({'file':rel,'lines':len(text.splitlines()),'test_functions':tf})
 report={'schema_version':1,'python_files':len(files),'python_lines':lines,'functions':functions,'test_functions':tests,'findings':findings,'files':files,
         'note':'This static inventory is not a substitute for review, tests, or threat modeling.'}
 out=ns.output or root/'docs'/'source-quality-audit.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
 md=['# Source-quality audit','',report['note'],'',f"- Python files: {len(files)}",f"- Python lines: {lines}",f"- Functions: {functions}",f"- Test functions: {tests}",f"- Flagged constructs: {len(findings)}",'']
 if findings:md+=['| Kind | Source |','|---|---|']+[f"| {x['kind']} | `{x['file']}:{x['line']}` |" for x in findings]
 out.with_suffix('.md').write_text('\n'.join(md)+'\n')
if __name__=='__main__':main()
