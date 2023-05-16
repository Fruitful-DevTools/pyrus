import unittest
from pyrus import cache


class TestCache(unittest.TestCase):

    def setUp(self):
        self.cache = cache.Cache()

    def test_get(self):
        self.cache.set("key1", "value1")
        self.assertEqual(self.cache.get("key1"), "value1")

    def test_set(self):
        self.cache.set("key1", "value1")
        self.assertEqual(self.cache.get("key1"), "value1")

    def test_del(self):
        self.cache.set("key1", "value1")
        self.cache.delete("key1")
        self.assertIsNone(self.cache.get("key1"))

    def tearDown(self):
        self.cache.delete("key1")


if __name__ == "__main__":
    unittest.main()