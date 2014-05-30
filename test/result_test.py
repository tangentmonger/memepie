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
        r.add("foo", Source("handle", "what they twote about foo", "twitter.com/linktotweet"))
        s = r.get_source_list("foo")
        self.assertEqual(s[0].handle, "handle")
        self.assertEqual(s[0].text, "what they twote about foo")
        self.assertEqual(s[0].link, "twitter.com/linktotweet")

if __name__ == "__main__":
    unittest.main()
