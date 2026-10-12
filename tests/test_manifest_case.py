"""Owned in-memory metadata regression; no ZIP bytes, extraction, or file writes."""
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch
from zipfile import ZipInfo
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import archive_producer as ap
import archive_checker as ac
from producer import infer
from checker import verify


def fake_archive(entries):
    archive = MagicMock()
    archive.__enter__.return_value = archive
    members = []
    payloads = {}
    for name, payload in entries:
        member = ZipInfo(name)
        member.file_size = len(payload)
        members.append(member)
        payloads[id(member)] = payload
    archive.infolist.return_value = members
    archive.read.side_effect = lambda member: payloads[id(member)]
    return archive


def fake_path():
    path = MagicMock()
    path.exists.return_value = True
    path.is_file.return_value = True
    path.stat.return_value = SimpleNamespace(st_size=0)
    return path


class ManifestCaseTests(unittest.TestCase):
    def test_only_exact_manifest_is_excluded(self):
        for module, read in ((ap, ap.read_archive), (ac, ac.unpack_archive)):
            archive = fake_archive([('META-INF/MANIFEST.MF', b'owned')])
            with self.subTest(adapter=module.__name__), \
                    patch.object(module, 'Path', return_value=fake_path()), \
                    patch.object(module, 'ZipFile', return_value=archive):
                self.assertEqual(read('owned-placeholder'), {})
            archive.read.assert_not_called()

    def test_case_distinct_names_remain_payload_keys(self):
        for name in ('META-INF/manifest.mf', 'meta-inf/MANIFEST.MF',
                     'Meta-Inf/Manifest.Mf'):
            for module, read in ((ap, ap.read_archive), (ac, ac.unpack_archive)):
                archive = fake_archive([(name, b'owned')])
                with self.subTest(name=name, adapter=module.__name__), \
                        patch.object(module, 'Path', return_value=fake_path()), \
                        patch.object(module, 'ZipFile', return_value=archive):
                    self.assertEqual(read('owned-placeholder'), {name: b'owned'})
                    archive.read.assert_called_once()

    def test_case_distinct_duplicate_keys_remain_rejected(self):
        name = 'META-INF/manifest.mf'
        for module, read, error in ((ap, ap.read_archive, ap.ArchiveInputError),
                                    (ac, ac.unpack_archive, ac.ArchiveRejected)):
            archive = fake_archive([(name, b'a'), (name, b'b')])
            with self.subTest(adapter=module.__name__), \
                    patch.object(module, 'Path', return_value=fake_path()), \
                    patch.object(module, 'ZipFile', return_value=archive), \
                    self.assertRaises(error):
                read('owned-placeholder')

    def test_case_distinct_probe_keeps_global_order_information(self):
        # Both providers have the same target. The ordinary case-distinct file
        # is a differing probe, and therefore must constrain the shared order.
        entries = [
            [('target.bin', b'equal'), ('META-INF/manifest.mf', b'a')],
            [('target.bin', b'equal'), ('META-INF/manifest.mf', b'b')],
            [('target.bin', b'equal'), ('META-INF/manifest.mf', b'a')],
        ]
        with patch.object(ap, 'Path', return_value=fake_path()), \
                patch.object(ap, 'ZipFile', side_effect=[fake_archive(x) for x in entries]):
            left = ap.lower_archives([('a', 'developer', 'a'),
                                      ('b', 'lib:b', 'b')], 'observed')
        with patch.object(ac, 'Path', return_value=fake_path()), \
                patch.object(ac, 'ZipFile', side_effect=[fake_archive(x) for x in entries]):
            right = ac.interpret_archives([
                {'id': 'a', 'owner': 'developer', 'path': 'a'},
                {'id': 'b', 'owner': 'lib:b', 'path': 'b'}], 'observed')
        self.assertEqual(left, right)
        self.assertEqual({row['key'] for row in left['rows']},
                         {'target.bin', 'META-INF/manifest.mf'})
        answer = verify(right, infer(left))
        self.assertEqual(answer['status'], 'classified')
        self.assertTrue(all(row['owners'] == ['developer'] for row in answer['regions']))


if __name__ == '__main__':
    unittest.main()
