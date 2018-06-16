
import os
import pathlib
import unittest

from encrypted_config.path_tools import normalize_path


class Tests(unittest.TestCase):

    def test_normalize_path(self):
        examples = [
            pathlib.Path(os.environ['HOME'], 'my_dir'),
            pathlib.Path('$HOME', 'my_dir'),
            pathlib.Path('~', 'my_dir')]
        reference = examples[0]
        reference_str = str(reference)
        for example in examples:
            example_str = str(example)
            result_str = normalize_path(example_str)
            self.assertEqual(reference_str, result_str)
            result = normalize_path(example)
            self.assertEqual(reference, result)
