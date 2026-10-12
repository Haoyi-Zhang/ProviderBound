"""Metadata-only admission checks; no malformed ZIP is constructed or executed."""
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import MagicMock, patch
from zipfile import ZipInfo
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
import archive_producer as ap
import archive_checker as ac
from producer import infer, normalize
from checker import read_model, verify


class ArchiveMetadataTests(unittest.TestCase):
    def reject_member(self, member):
        for validate, error in ((ap._member_name, ap.ArchiveInputError),
                                (ac._entry_key, ac.ArchiveRejected)):
            with self.subTest(adapter=validate.__module__), self.assertRaises(error):
                validate(member)

    def test_unchanged_file_and_directory_metadata(self):
        for name in ('note.bin', 'folder/note.bin', 'folder/', 'space name'):
            member = ZipInfo(name)
            self.assertEqual(ap._member_name(member), name)
            self.assertEqual(ac._entry_key(member), name)

    def test_nul_in_original_metadata_is_rejected(self):
        member = ZipInfo('note.bin')
        member.orig_filename = 'note.bin\x00suffix'
        self.reject_member(member)

    def test_unchanged_nul_metadata_is_also_rejected(self):
        member = ZipInfo('note.bin')
        member.orig_filename = member.filename = 'note\x00.bin'
        self.reject_member(member)

    def test_changed_spelling_is_not_canonicalized(self):
        member = ZipInfo('folder/note.bin')
        member.orig_filename = 'folder\\note.bin'
        self.reject_member(member)

    def test_invalid_original_relative_names(self):
        for name in ('', '/note.bin', '../note.bin', 'folder//note.bin',
                     'folder/./note.bin', 'folder//', '/'):
            member = ZipInfo('note.bin')
            member.orig_filename = member.filename = name
            self.reject_member(member)

    def test_adapters_validate_before_manifest_or_directory_filter(self):
        # A fake archive supplies only metadata; payload reads must never occur.
        with TemporaryDirectory() as directory:
            path = Path(directory) / 'placeholder.zip'
            path.touch()
            for name in ('note.bin', 'folder/', 'META-INF/MANIFEST.MF'):
                member = ZipInfo(name)
                member.orig_filename = name + '\x00suffix'
                for module, read, error in ((ap, ap.read_archive, ap.ArchiveInputError),
                                            (ac, ac.unpack_archive, ac.ArchiveRejected)):
                    archive = MagicMock()
                    archive.__enter__.return_value = archive
                    archive.infolist.return_value = [member]
                    with self.subTest(name=name, adapter=module.__name__), \
                            patch.object(module, 'ZipFile', return_value=archive), \
                            self.assertRaises(error):
                        read(path)
                    archive.read.assert_not_called()

    def test_valid_excluded_members_do_not_read_payloads(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / 'placeholder.zip'
            path.touch()
            for module, read in ((ap, ap.read_archive), (ac, ac.unpack_archive)):
                archive = MagicMock()
                archive.__enter__.return_value = archive
                archive.infolist.return_value = [ZipInfo('folder/'), ZipInfo('META-INF/MANIFEST.MF')]
                with patch.object(module, 'ZipFile', return_value=archive):
                    self.assertEqual(read(path), {})
                archive.read.assert_not_called()

    def test_symbolic_inventory_names_are_not_archive_admission(self):
        name = 'symbolic//entry'
        raw = {'kind': 'inventory', 'before': [],
               'providers': [{'id': 'p', 'owner': 'lib:p', 'relocations': [],
                              'entries': [{'name': name, 'payload': '00'}]}],
               'observed': [{'name': name, 'payload': '00'}]}
        self.assertEqual(normalize(raw), read_model(raw))
        self.assertEqual(verify(raw, infer(raw))['regions'][0]['key'], name)
        self.reject_member(ZipInfo(name))


if __name__ == '__main__':
    unittest.main()
