"""Owned checkout metadata only; no Git invocation, real config, or pointer reads."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import release_manifest
import reproduce_release


class ReleaseManifestTests(unittest.TestCase):
    def fixture(self, root):
        entries = {'payload.txt': b'owned payload', '.gitignore': b'owned ignore text',
                   '.gitattributes': b'owned attributes text', '.gitkeep': b'owned ordinary file',
                   '.github/workflows/check.yml': b'owned workflow placeholder',
                   '.git-backup/note.txt': b'owned ordinary directory',
                   'nested/payload.txt': b'owned nested payload'}
        for name, value in entries.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(value)
        manifest = root / 'RELEASE-MANIFEST.sha256'
        manifest.write_text(''.join(f'{release_manifest.sha(path)}  {name}\n'
                                    for name, path in release_manifest.files(root)), encoding='utf-8')
        return set(entries)

    def check_consumer(self, root):
        with patch.object(reproduce_release, 'ROOT', root), redirect_stdout(StringIO()):
            reproduce_release.verify_manifest()

    def test_git_directory_excluded_without_ignoring_artifact_files(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            expected = self.fixture(root)
            for name in ('.git/HEAD', '.git/config', 'nested/.git/HEAD'):
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(b'owned metadata placeholder')
            self.assertEqual({name for name, _ in release_manifest.files(root)}, expected)
            self.check_consumer(root)
            (root / 'unlisted.txt').write_bytes(b'owned ordinary new artifact')
            self.assertIn('unlisted.txt', {name for name, _ in release_manifest.files(root)})
            with self.assertRaisesRegex(ValueError, 'membership differs'):
                self.check_consumer(root)

    def test_git_pointer_file_excluded_without_weakening_hash_checks(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            expected = self.fixture(root)
            (root / '.git').write_bytes(b'gitdir: owned-placeholder-never-followed\n')
            self.assertEqual({name for name, _ in release_manifest.files(root)}, expected)
            self.check_consumer(root)
            (root / 'payload.txt').write_bytes(b'changed owned payload')
            with self.assertRaisesRegex(ValueError, 'manifest content differs'):
                self.check_consumer(root)


if __name__ == '__main__':
    unittest.main()
