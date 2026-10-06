"""Finite regressions for witness reuse, byte lowering, and fresh execution."""
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
import json, sys, unittest
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'src'))
sys.path.insert(0, str(ROOT/'scripts'))
import producer, telemetry
from checker import verify, read_model
from archive_producer import _safe_name
from archive_checker import _name_ok
from reproduce import prepare_output, compare_generated
from make_inputs import main as make_inputs
from public_corpus import _process_pair, certificate_sizes


class CompletionTests(unittest.TestCase):
    def test_even_certificate_sample_uses_two_middle_values(self):
        self.assertEqual(certificate_sizes([10, 20])['certificate_bytes_median'], 15)
        self.assertEqual(certificate_sizes([1, 10, 20, 100])['certificate_bytes_median'], 15)

    def test_reuse_world_across_different_candidate_sets(self):
        raw = {'kind': 'graph', 'owners': ['developer', 'lib:A', 'lib:B'], 'before': [],
               'rows': [{'key': 'r', 'present': [0, 1], 'good': [0, 1]},
                        {'key': 's', 'present': [0, 1, 2], 'good': [0, 1, 2]}]}
        with patch.object(producer, 'search', wraps=producer.search) as search:
            cert = producer.infer(raw)
        self.assertEqual(search.call_count, 3)
        self.assertEqual(len(cert['orders']), 3)
        answer = verify(raw, cert)
        self.assertEqual(answer['regions'][1]['owners'], ['developer', 'lib:A', 'lib:B'])

    def test_byte_equality_is_not_a_digest_premise(self):
        raw = {'kind': 'inventory', 'before': [],
               'providers': [{'id': 'a', 'owner': 'developer', 'relocations': [],
                              'entries': [{'name': 'x', 'payload': '00'}]},
                             {'id': 'b', 'owner': 'lib:B', 'relocations': [],
                              'entries': [{'name': 'x', 'payload': '01'}]}],
               'observed': [{'name': 'x', 'payload': '00'}]}
        with patch('hashlib.sha256', side_effect=AssertionError('digest must not determine equality')):
            self.assertEqual(producer.normalize(raw), read_model(raw))
            self.assertEqual(verify(raw, producer.infer(raw))['regions'][0]['owners'], ['developer'])

    def test_archive_path_grammar_agrees_without_normalizing_spelling(self):
        for name in ('a/x.bin', 'a.b/x', 'space name', 'a//x', 'a/./x', 'a/'):
            with self.subTest(name=name):
                self.assertEqual(_safe_name(name), _name_ok(name))
        self.assertFalse(_safe_name('a//x'))
        self.assertFalse(_safe_name('a/./x'))

    def test_unavailable_rss_is_null(self):
        with patch.object(telemetry, 'resource', None):
            self.assertIsNone(telemetry.usage()['peak_rss_kib'])
            self.assertIsNone(telemetry.usage(children=True)['cpu_seconds'])

    def test_nonempty_output_is_rejected_without_overwrite(self):
        with TemporaryDirectory() as directory:
            output = prepare_output(Path(directory)/'run')
            marker = output/'reproduction_summary.json'
            marker.write_text('{"old": true}', encoding='utf-8')
            with self.assertRaises(ValueError):
                prepare_output(output)
            self.assertEqual(json.loads(marker.read_text()), {'old': True})

    def test_fresh_fixture_regeneration_matches_all_retained_inputs(self):
        with TemporaryDirectory() as directory:
            output = Path(directory)/'inputs'
            make_inputs(output)
            self.assertEqual(compare_generated(output), 61)

    def test_owned_archive_pair_replays_serialized_certificates(self):
        import public_corpus
        from checker import load
        with TemporaryDirectory() as directory:
            base = Path(directory); jars = base/'jars'; outputs = base/'outputs'; retained = base/'retained'
            jars.mkdir(); outputs.mkdir()
            for name, value in (('a.jar', b'a'), ('b.jar', b'b')):
                with ZipFile(jars/name, 'w') as archive:
                    archive.writestr('target.bin', b'same'); archive.writestr('probe.bin', value)
            for suffix, value in (('ab', b'a'), ('ba', b'b')):
                with ZipFile(outputs/f'owned-{suffix}.zip', 'w') as archive:
                    archive.writestr('target.bin', b'same'); archive.writestr('probe.bin', value)
            record = {'pair_id': 'owned', 'left': 'a.jar', 'right': 'b.jar', 'kind': 'mixed'}
            with patch.object(public_corpus, 'load_certificate', wraps=load) as loader:
                result = _process_pair((record, str(jars), str(outputs), str(retained)))
            self.assertEqual(loader.call_count, 2)
            self.assertEqual(result['counts']['oracle_mismatch'], 0)
            self.assertEqual(result['counts']['narrow'], 2)
            self.assertEqual(result['counts']['ant_mismatch'], 0)  # content check, no Ant execution
            for suffix in ('ab', 'ba'):
                self.assertTrue((outputs/f'owned-{suffix}.certificate.json').is_file())


if __name__ == '__main__':
    unittest.main()
