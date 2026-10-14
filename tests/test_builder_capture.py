"""Owned builder diagnostics, without executing any provider classes."""
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from public_corpus import run_builder


class BuilderCaptureTests(unittest.TestCase):
    def test_localized_streams_are_preserved_without_a_text_reader(self):
        result=subprocess.CompletedProcess(['java'],0,'完成'.encode('gbk'),'警告'.encode('gbk'))
        with TemporaryDirectory() as folder, patch('public_corpus.subprocess.run',return_value=result) as run:
            run_builder(['java'],Path(folder))
            self.assertEqual((Path(folder)/'builder.stdout.bin').read_bytes(),result.stdout)
            self.assertEqual((Path(folder)/'builder.stderr.bin').read_bytes(),result.stderr)
            self.assertNotIn('text',run.call_args.kwargs)

    def test_builder_error_is_not_reported_as_a_successful_build(self):
        result=subprocess.CompletedProcess(['java'],1,b'context',b'failed')
        with TemporaryDirectory() as folder, patch('public_corpus.subprocess.run',return_value=result):
            with self.assertRaisesRegex(RuntimeError,'Apache Ant failed: 1'):
                run_builder(['java'],Path(folder))
            self.assertEqual((Path(folder)/'builder.stderr.bin').read_bytes(),b'failed')
