"""Owned compiler-output contract: raw diagnostics and exact numeric stdout."""
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from java_pilot import invoke


class JavaCaptureTests(unittest.TestCase):
    def test_optimized_invocation_stops_before_fixture_creation(self):
        script=Path(__file__).resolve().parents[1]/'scripts/java_pilot.py'
        with TemporaryDirectory() as folder:
            output=Path(folder)/'owned-java'
            result=subprocess.run([sys.executable,'-O',str(script),str(output)],
                                  capture_output=True,timeout=10)
            self.assertNotEqual(result.returncode,0)
            self.assertIn(b'Run without Python -O/-OO.',result.stderr)
            self.assertFalse(output.exists())

    def test_host_locale_diagnostics_are_retained_as_bytes(self):
        diagnostic='警告'.encode('gbk')
        result=subprocess.CompletedProcess(['javac'],0,b'',diagnostic)
        with TemporaryDirectory() as folder, patch('java_pilot.subprocess.run',return_value=result) as run:
            self.assertEqual(invoke(['javac'],log_directory=folder,name='compile'),'')
            self.assertEqual((Path(folder)/'compile.stderr.bin').read_bytes(),diagnostic)
            self.assertEqual(json.loads((Path(folder)/'compile.json').read_text())['returncode'],0)
            self.assertNotIn('text',run.call_args.kwargs)

    def test_nonzero_compiler_exit_preserves_output_before_raising(self):
        result=subprocess.CompletedProcess(['javac'],1,b'context',b'diagnostic')
        with TemporaryDirectory() as folder, patch('java_pilot.subprocess.run',return_value=result):
            with self.assertRaises(subprocess.CalledProcessError):
                invoke(['javac'],log_directory=folder,name='compile')
            self.assertEqual((Path(folder)/'compile.stdout.bin').read_bytes(),b'context')
            self.assertEqual((Path(folder)/'compile.stderr.bin').read_bytes(),b'diagnostic')

    def test_numeric_probe_does_not_replace_invalid_stdout(self):
        result=subprocess.CompletedProcess(['java'],0,b'\xff',b'')
        with patch('java_pilot.subprocess.run',return_value=result):
            with self.assertRaises(UnicodeDecodeError):
                invoke(['java'])
