import unittest


class SuccessCase(unittest.TestCase):

    def test_good(self):
        self.assertTrue(1)

    def test_best(self):
        self.assertTrue(2)

class FailureCase(unittest.TestCase):

    def test_bad(self):
        self.assertFalse(1)

class ErrorCase(unittest.TestCase):

    def test_ough(self):
        raise ValueError('something wrong')
