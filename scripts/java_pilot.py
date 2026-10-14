"""Benign owned Java integration: compile, first-winner ZIP, reconstruct and replay.

This tests exact class-file bytes without bytecode relocation. It neither invokes
Maven Shade nor exercises Android, third-party services, or vulnerabilities.
"""
from pathlib import Path
import json, shutil, subprocess, sys, tempfile, time, zipfile
from telemetry import usage
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from producer import infer
from checker import verify, load
ROOT=Path(__file__).resolve().parents[1]

MARKER='package demo; public final class Marker { public static String text() { return "shared"; } }\n'
PROBE='package demo; public final class Probe { public static int value() { return VALUE; } }\n'
DRIVER='public final class Readback { public static void main(String[] args) { System.out.println(demo.Probe.value()); } }\n'

def invoke(args, *, log_directory=None, name=None):
    # javac diagnostics follow the host locale and are not the numeric probe.
    # Retain bytes rather than losing a reader thread to an implicit decoder.
    completed=subprocess.run(args,check=False,capture_output=True,timeout=30)
    if log_directory is not None:
        directory=Path(log_directory)
        directory.mkdir(parents=True,exist_ok=True)
        (directory/(name+'.stdout.bin')).write_bytes(completed.stdout)
        (directory/(name+'.stderr.bin')).write_bytes(completed.stderr)
        (directory/(name+'.json')).write_text(json.dumps(
            {'argv':list(args),'returncode':completed.returncode,
             'stdout_bytes':len(completed.stdout),'stderr_bytes':len(completed.stderr)},
            indent=2)+'\n',encoding='utf-8')
    completed.check_returncode()
    # The owned program's documented output is an ASCII integer; do not
    # replace invalid bytes and accidentally accept a changed observation.
    return completed.stdout.decode('ascii').strip()

def write_jar(path, entries):
    with zipfile.ZipFile(path,'w',compression=zipfile.ZIP_STORED) as z:
        for name,payload in sorted(entries.items()):
            info=zipfile.ZipInfo(name,date_time=(2000,1,1,0,0,0)); info.external_attr=0o644<<16
            z.writestr(info,payload)

def read_jar(path):
    with zipfile.ZipFile(path) as z:
        names=z.namelist(); assert len(names)==len(set(names))
        return {name:z.read(name) for name in names}

def run(output):
    if not __debug__:
        raise RuntimeError('Run without Python -O/-OO.')
    if not shutil.which('javac') or not shutil.which('java'):
        raise RuntimeError('Java development tools required for this explicitly documented integration command')
    output=Path(output); (output/'java').mkdir(parents=True,exist_ok=True)
    sources=output/'java/sources'; sources.mkdir(parents=True,exist_ok=True)
    command_logs=output/'java/logs'
    t=time.process_time(); children_before=usage(children=True); wall=time.monotonic()
    with tempfile.TemporaryDirectory(prefix='boundary-owned-java-') as work:
        work=Path(work); providers=[]
        for i,value in enumerate((11,22)):
            src=sources/f'p{i}'/'demo'; src.mkdir(parents=True,exist_ok=True)
            (src/'Marker.java').write_text(MARKER); (src/'Probe.java').write_text(PROBE.replace('VALUE',str(value)))
            classes=work/f'p{i}'; classes.mkdir()
            invoke(['javac','-J-Xmx256m','-J-XX:ActiveProcessorCount=1','-J-XX:+UseSerialGC','-J-Xint','--release','8','-g:none','-d',str(classes),str(src/'Marker.java'),str(src/'Probe.java')],
                   log_directory=command_logs,name=f'compile-p{i}')
            entries={str(p.relative_to(classes)).replace('\\','/'):p.read_bytes() for p in classes.rglob('*.class')}
            jar=output/'java'/f'p{i}.jar'; write_jar(jar,entries); providers.append(read_jar(jar))
        assert providers[0]['demo/Marker.class']==providers[1]['demo/Marker.class']
        assert providers[0]['demo/Probe.class']!=providers[1]['demo/Probe.class']
        (sources/'Readback.java').write_text(DRIVER)
        driver=work/'driver'; driver.mkdir()
        invoke(['javac','-J-Xmx256m','-J-XX:ActiveProcessorCount=1','-J-XX:+UseSerialGC','-J-Xint','--release','8','-g:none','-cp',str(output/'java/p0.jar'),'-d',str(driver),str(sources/'Readback.java')],
               log_directory=command_logs,name='compile-driver')
        records=[]
        for i,order in enumerate(((0,1),(1,0))):
            merged={}
            for p in order:
                for key,value in providers[p].items(): merged.setdefault(key,value)
            jar=output/'java'/f'b{i}.jar'; write_jar(jar,merged); observed=read_jar(jar)
            import os
            value=invoke(['java','-Xmx128m','-XX:ActiveProcessorCount=1','-XX:+UseSerialGC','-Xint','-cp',os.pathsep.join((str(driver),str(jar))),'Readback'],
                         log_directory=command_logs,name=f'probe-{i}')
            assert value==str((11,22)[order[0]])
            raw={'kind':'inventory','providers':[
                 {'id':f'p{j}','owner':['developer','lib:example'][j],'relocations':[],
                  'entries':[{'name':key,'payload':data.hex()} for key,data in sorted(entries.items())]}
                 for j,entries in enumerate(providers)],'before':[],
                 'observed':[{'name':key,'payload':data.hex()} for key,data in sorted(observed.items())]}
            cert=infer(raw); raw_path=output/'java'/f'b{i}.input.json'; cert_path=output/'java'/f'b{i}.certificate.json'
            raw_path.write_text(json.dumps(raw,indent=2)+'\n'); cert_path.write_text(json.dumps(cert,indent=2)+'\n')
            result=verify(load(raw_path),load(cert_path))
            target=next(r for r in result['regions'] if r['key']=='demo/Marker.class')
            assert target['owners']==[['developer'],['lib:example']][i]
            # Exact-byte local evidence alone cannot distinguish Marker.class.
            records.append({'case':f'j{i+1:03}','assembly_order':list(order),'runtime_probe_value':int(value),
                            'marker_byte_candidates':2,'marker_owners':target['owners'],'status':result['status'],
                            'input_bytes':raw_path.stat().st_size,'certificate_bytes':cert_path.stat().st_size})
    after=usage(children=True)
    parent_cpu=time.process_time()-t
    child_cpu=(after['cpu_seconds']-children_before['cpu_seconds']
               if after['cpu_seconds'] is not None and children_before['cpu_seconds'] is not None else None)
    summary={'scope':'two owned Java builds; no public projects, Maven execution, or Android pipeline',
             'cases':records,'cpu_seconds':parent_cpu+child_cpu if child_cpu is not None else None,
             'process_cpu_seconds':parent_cpu, 'child_cpu_seconds':child_cpu,
             'wall_seconds':time.monotonic()-wall,'parent_peak_rss_kib':usage()['peak_rss_kib'],
             'child_peak_rss_kib':after['peak_rss_kib'], 'rss_scope':after['scope'],
             'byte_reproduction':'Exact consumed class bytes are retained in these JARs and JSON inventories. Recompilation need not be byte-identical across different compilers; semantic assertions must agree.'}
    (output/'java_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    return summary
if __name__=='__main__': print(json.dumps(run(sys.argv[1] if len(sys.argv)>1 else ROOT/'results'),indent=2))
