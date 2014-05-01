import unittest
from parser import Parser
from meme import Meme

class ParserTest(unittest.TestCase):

    def test_generates_valid_regex(self):
        p = Parser()
        m = Meme("all your * -base")
        self.assertEqual(p._format_regex(m), "all your ([\\w'\\-]+)")

    def test_collates_words(self):
        p = Parser()
        m = Meme("all your * -base")
        t = ["all your cake", "all your cake", "all your data"]
        self.assertEqual(p.collate_words(m, t), {"cake":2, "data":1})

    def test_handles_no_matches(self):
        p = Parser()
        m = Meme("all your * -base")
        t = ["foo", "bar", "baz"]
        self.assertEqual(p.collate_words(m, t), {})

    def test_converts_to_lowercase(self):
        p = Parser()
        m = Meme("all your * -base")
        t = ["ALL YOUR DATA"]
        self.assertEqual(p.collate_words(m, t), {"data":1})
        
if __name__ == "__main__":
    unittest.main()
