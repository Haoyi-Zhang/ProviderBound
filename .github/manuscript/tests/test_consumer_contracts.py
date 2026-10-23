"""Benign result-consumer regressions; private fixtures, no native experiments."""
from copy import deepcopy
import ast
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / 'artifact'
sys.path.insert(0, str(ART / 'scripts'))
import audit_claims
from manuscript_inputs import validate_diagnostic_inputs


class ConsumerContractTests(unittest.TestCase):
    def fixture(self):
        holder = tempfile.TemporaryDirectory(prefix='p010-consumer-')
        self.addCleanup(holder.cleanup)
        root = Path(holder.name)
        shutil.copytree(ART, root / 'artifact')
        (root / 'paper').mkdir()
        shutil.copy2(ROOT / 'paper/build_tables.py', root / 'paper/build_tables.py')
        shutil.copy2(ROOT / 'paper/retained_test_coverage.py', root / 'paper/retained_test_coverage.py')
        return root

    def mapping(self, root):
        path = root / 'artifact/results/diagnostics/current/input-source-sha256.json'
        return path, json.loads(path.read_text(encoding='utf-8'))

    def rejected_binding(self, root):
        with self.assertRaises((ValueError, RuntimeError, OSError)):
            validate_diagnostic_inputs(root / 'artifact')
        self.assertEqual(audit_claims.audit(root / 'artifact')['status'], 'FAIL')

    def export(self, root):
        return subprocess.run([sys.executable, '-B', str(root / 'paper/build_tables.py')],
                              cwd=root / 'paper', capture_output=True, timeout=30)

    def test_retained_catalogue_accepts_history_without_rehashing_auditors(self):
        root = self.fixture()
        path, mapping = self.mapping(root)
        before = path.read_bytes()
        result = validate_diagnostic_inputs(root / 'artifact')
        self.assertEqual(result['catalogue_entries'], 165)
        self.assertEqual(result['current_file_bindings_checked'], 163)
        self.assertEqual(set(result['historical_program_bindings']),
                         {'scripts/audit_claims.py', 'tests/test_audit_claims.py'})
        self.assertEqual(path.read_bytes(), before)
        self.assertEqual(mapping['scripts/audit_claims.py'],
                         '3eb27d11e0b3785b2a832c772587112d04115497b8ae45f8ac284d4d0bf345ac')
        self.assertEqual(audit_claims.audit(root / 'artifact')['status'], 'PASS')
        exported = self.export(root)
        self.assertEqual(exported.returncode, 0, exported.stderr.decode(errors='replace'))

    def test_empty_catalogue_fails_both_consumers(self):
        root = self.fixture()
        path, _ = self.mapping(root)
        path.write_text('{}', encoding='utf-8')
        self.rejected_binding(root)
        self.assertNotEqual(self.export(root).returncode, 0)
        self.assertFalse((root / 'paper/result_macros.tex').exists())

    def test_missing_previously_noncore_member_is_not_optional(self):
        root = self.fixture()
        path, value = self.mapping(root)
        del value['inputs/fixtures/f001.json']
        path.write_text(json.dumps(value), encoding='utf-8')
        self.rejected_binding(root)

    def test_duplicate_catalogue_keys_fail_even_if_values_agree(self):
        root = self.fixture()
        path, value = self.mapping(root)
        text = path.read_text(encoding='utf-8')
        key = 'inputs/fixtures/f001.json'
        path.write_text(text.rstrip()[:-1] + ',"' + key + '":"' + value[key] + '"}', encoding='utf-8')
        self.rejected_binding(root)

    def test_bad_digest_and_absent_catalogue_fail_closed(self):
        for bad in (False, 123, 'g' * 64, '00', 'A' * 64):
            root = self.fixture()
            path, value = self.mapping(root)
            value['src/producer.py'] = bad
            path.write_text(json.dumps(value), encoding='utf-8')
            with self.subTest(bad=bad):
                self.rejected_binding(root)
        path.unlink()
        self.rejected_binding(root)

    def test_current_scientific_change_cannot_inherit_historical_receipt(self):
        root = self.fixture()
        path = root / 'artifact/src/producer.py'
        path.write_bytes(path.read_bytes() + b'\n# benign identity change\n')
        self.rejected_binding(root)

    def test_rehashing_scientific_change_does_not_rewrite_history(self):
        import hashlib
        root = self.fixture()
        source = root / 'artifact/src/producer.py'
        source.write_bytes(source.read_bytes() + b'\n# benign identity change\n')
        path, value = self.mapping(root)
        value['src/producer.py'] = hashlib.sha256(source.read_bytes()).hexdigest()
        path.write_text(json.dumps(value), encoding='utf-8')
        self.rejected_binding(root)

    def test_rate_mean_denominator_and_extrema_corruption_are_rejected(self):
        changes = [('oracle_exact_rate', 0.123456), ('oracle_conservative_rate', 0.5),
                   ('hidden_winner_coverage_rate', 0.5), ('mean_owner_set_size', 1.1),
                   ('observations', True), ('oracle_exact_count', True)]
        for field, bad in changes:
            root = self.fixture()
            path = root / 'artifact/results/current/public/summary.json'
            value = json.loads(path.read_text(encoding='utf-8'))
            value['baseline_comparison_on_collision_regions']['local_bytes'][field] = bad
            path.write_text(json.dumps(value), encoding='utf-8')
            with self.subTest(field=field):
                self.assertEqual(audit_claims.audit(root / 'artifact')['status'], 'FAIL')
                self.assertNotEqual(self.export(root).returncode, 0)
                self.assertFalse((root / 'paper/baseline_table.tex').exists())
        root = self.fixture()
        path = root / 'artifact/results/current/public/summary.json'
        value = json.loads(path.read_text(encoding='utf-8'))
        value['certificate_bytes_max'] += 1
        path.write_text(json.dumps(value), encoding='utf-8')
        self.assertEqual(audit_claims.audit(root / 'artifact')['status'], 'FAIL')

    def test_owner_mean_corruption_is_rejected_even_in_both_summaries(self):
        root = self.fixture()
        for relative in ('results/owner-granularity.json',
                         'results/diagnostics/current/owner-granularity.json'):
            path = root / 'artifact' / relative
            value = json.loads(path.read_text(encoding='utf-8'))
            value['metrics']['debian_package']['local_mean_set_size'] = 1.5
            path.write_text(json.dumps(value), encoding='utf-8')
        self.assertEqual(audit_claims.audit(root / 'artifact')['status'], 'FAIL')

    def test_build_requires_python_vector_consumer_before_tex(self):
        spec = importlib.util.spec_from_file_location('p010_paper_build', ROOT / 'paper/build.py')
        build = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(build)
        commands = []
        class PlotReached(RuntimeError):
            pass
        def run(command):
            commands.append(command)
            if any('plot_numeric.py' in str(arg) for arg in command):
                raise PlotReached('owned plot failure')
            if str(command[0]).endswith('pdflatex'):
                raise RuntimeError('TeX reached without the required vector consumer')
            return ''
        with patch.object(build.shutil, 'which', side_effect=lambda name: name), \
                patch.object(build, 'run', side_effect=run), self.assertRaises(PlotReached):
            build.main()
        self.assertTrue(any('build_tables.py' in command for command in commands))
        plot = commands[-1]
        self.assertEqual(plot[0], sys.executable)
        self.assertIn('--output-dir', plot)

    def test_certificate_connector_enters_replay_not_lowering(self):
        source = ast.parse((ART / 'figures/draw_schematics.py').read_text(encoding='utf-8'))
        draw = next(node for node in source.body if isinstance(node, ast.FunctionDef) and node.name == 'draw')
        instances = []
        class Drawing:
            def __init__(self, bounds):
                self.arrows = []
                self.ax = SimpleNamespace(add_patch=lambda *a, **k: None)
                instances.append(self)
            def point(self, name, side):
                return name, side
            def arrow(self, p, q, **kwargs):
                self.arrows.append((p[0], q[0]))
            def edge(self, a, b, *args, **kwargs):
                self.arrows.append((a, b))
            def box(self, *args, **kwargs): pass
            def frame(self, *args, **kwargs): pass
            def text(self, *args, **kwargs): pass
            def save(self, *args, **kwargs): pass
        env = {'Drawing': Drawing, 'Rectangle': lambda *a, **k: None}
        exec(compile(ast.Module(body=[draw], type_ignores=[]), '<owned drawing contract>', 'exec'), env)
        env['draw'](Path('unused-no-write'))
        self.assertIn(('cert', 'checker'), instances[1].arrows)
        self.assertNotIn(('cert', 'lowerc'), instances[1].arrows)

    def test_companion_explanation_keeps_96_plus_four(self):
        text = (ART / 'docs/source-comparison.md').read_text(encoding='utf-8')
        self.assertNotIn('resolves 100 equal-byte observations', text)
        self.assertIn('96', text)
        self.assertIn('four', text)
        self.assertIn('p027', text)

    def test_paper_does_not_relabel_retained_test_execution_as_current(self):
        text = (ROOT / 'paper/sections/07-results.tex').read_text(encoding='utf-8')
        self.assertNotIn('current test definitions', text)
        self.assertNotIn('current bounded run passes', text)


if __name__ == '__main__':
    unittest.main()
