import unittest
import os


if os.environ.get('TESTION_SUCCESS', '1') == '1':
    class SuccessCase(unittest.TestCase):

        def test_good(self):
            self.assertTrue(1)

        def test_best(self):
            self.assertTrue(2)

if os.environ.get('TESTION_FAILURE', '1') == '1':
    class FailureCase(unittest.TestCase):

        def test_bad(self):
            self.assertFalse(1)

if os.environ.get('TESTION_ERROR', '1') == '1':
    class ErrorCase(unittest.TestCase):

        def test_ough(self):
            raise ValueError('something wrong')
