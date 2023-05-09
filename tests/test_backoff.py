import unittest
from pyrus import backoff

def test_function():
    raise ValueError("Test Exception")


class TestBackoff(unittest.TestCase):

    def test_backoff(self):
        self.assertEqual(backoff.backoff(test_function, 5, 1), 2)

unittest.main()