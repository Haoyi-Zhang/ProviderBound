"""Owned portability/admission control; no compiler or provider execution."""
from pathlib import Path
import importlib
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))


class JavaPortabilityTests(unittest.TestCase):
    def test_no_posix_resource_reaches_explicit_jdk_admission(self):
        # Windows lacks resource. Simulate that fact even on POSIX hosts.
        # No output is created: JDK admission must precede fixture writes.
        sys.modules.pop('java_pilot', None)
        with patch.dict(sys.modules, {'resource': None}):
            module = importlib.import_module('java_pilot')
            with patch.object(module.shutil, 'which', return_value=None):
                with self.assertRaisesRegex(RuntimeError, 'Java development tools required'):
                    module.run(Path(__file__).resolve().parents[1] / 'results/never-created-jdk-control')


if __name__ == '__main__':
    unittest.main()
