"""Owned PDF-selection controls; no build, archive or upstream execution."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ART = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('owned_release_gate', ART/'scripts/final_release_gate.py')
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

class PrimaryPdfGateTests(unittest.TestCase):
    def test_missing_primary_cannot_select_a_figure(self):
        with tempfile.TemporaryDirectory(dir=ART) as directory:
            paper=Path(directory)
            (paper/'figure.pdf').write_bytes(b'owned placeholder')
            with patch.object(gate,'PAPER',paper), patch.object(gate,'run') as run:
                with self.assertRaises(RuntimeError): gate.find_pdf()
                run.assert_not_called()

    def test_only_named_primary_is_inspected(self):
        with tempfile.TemporaryDirectory(dir=ART) as directory:
            paper=Path(directory)
            (paper/'main.pdf').write_bytes(b'owned placeholder')
            (paper/'another.pdf').write_bytes(b'owned placeholder')
            with patch.object(gate,'PAPER',paper), patch.object(gate,'run',return_value='Pages: 36\n') as run:
                self.assertEqual(paper/'main.pdf',gate.find_pdf())
                self.assertEqual(['pdfinfo',str(paper/'main.pdf')],run.call_args.args[0])

    def test_bad_page_metadata_and_tool_failure_propagate(self):
        with tempfile.TemporaryDirectory(dir=ART) as directory:
            paper=Path(directory)
            (paper/'main.pdf').write_bytes(b'owned placeholder')
            for text in ('Pages: 0\n','no page count\n'):
                with patch.object(gate,'PAPER',paper), patch.object(gate,'run',return_value=text):
                    with self.assertRaises(RuntimeError): gate.find_pdf()
            with patch.object(gate,'PAPER',paper), patch.object(gate,'run',side_effect=RuntimeError('owned tool failure')):
                with self.assertRaisesRegex(RuntimeError,'owned tool failure'): gate.find_pdf()

if __name__=='__main__': unittest.main()
