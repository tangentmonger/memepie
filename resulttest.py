import unittest
from result import Result

class ResultTest(unittest.TestCase):

    def test_can_add_word(self):
        r = Result()
        r.add("foo")
        self.assertEqual(r.get_list(), [("foo", 1)])
        self.assertEqual(r.count, 1)

    def test_can_add_duplicate_words(self):
        r = Result()
        r.add("foo")
        r.add("foo")
        self.assertEqual(r.get_list(), [("foo", 2)])
        self.assertEqual(r.count, 2)

    def test_list_is_sorted(self):
        r = Result()
        r.add("baz")
        r.add("bar")
        r.add("foo")
        r.add("foo")
        r.add("baz")
        r.add("baz")
        self.assertEqual(r.get_list(), [("baz", 3), ("foo", 2), ("bar", 1)])
        
if __name__ == "__main__":
    unittest.main()
