import unittest
from result import Result
from source import Source

class ResultTest(unittest.TestCase):

    def test_can_add_word(self):
        r = Result()
        r.add("foo", None)
        self.assertEqual(r.get_list(), [("foo", 1)])
        self.assertEqual(r.count, 1)

    def test_can_add_duplicate_words(self):
        r = Result()
        r.add("foo", None)
        r.add("foo", None)
        self.assertEqual(r.get_list(), [("foo", 2)])
        self.assertEqual(r.count, 2)

    def test_list_is_sorted(self):
        r = Result()
        r.add("baz", None)
        r.add("bar", None)
        r.add("foo", None)
        r.add("foo", None)
        r.add("baz", None)
        r.add("baz", None)
        self.assertEqual(r.get_list(), [("baz", 3), ("foo", 2), ("bar", 1)])
        
    def test_sources_are_stored(self):
        r = Result()
        r.add("foo", Source("screen_name", "name", "1234567890", "what they twote about foo"))
        s = r.get_source_list("foo")
        self.assertEqual(s[0].handle_id, "screen_name")
        self.assertEqual(s[0].handle_text, "name")
        self.assertEqual(s[0].status_id, "1234567890")
        self.assertEqual(s[0].status_text, "what they twote about foo")

if __name__ == "__main__":
    unittest.main()
