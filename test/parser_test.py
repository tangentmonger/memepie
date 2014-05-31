import unittest
from meme import Meme
from result import Result
from source import Source
from src.parser import Parser #module name shadowing :(

class ParserTest(unittest.TestCase):

    def test_generates_valid_regex(self):
        p = Parser()
        m = Meme("all your * -base")
        self.assertEqual(p._format_regex(m), "all your ([\\w'\\-]+)")

    def test_generates_valid_weird_regex(self):
        p = Parser()
        m = Meme("amn't foo-bar * -isn't")
        self.assertEqual(p._format_regex(m), "amn't foo-bar ([\\w'\\-]+)")

    def test_collates_words(self):
        p = Parser()
        m = Meme("all your * -base")
        s = [Source("", "", "",  "all your cake"),
                Source("", "", "", "all your cake"), 
                Source("", "", "", "all your data")]
        self.assertEqual(p.collate_words(m, s).get_list(), [("cake",2), ("data",1)])

    def test_handles_no_matches(self):
        p = Parser()
        m = Meme("all your * -base")
        s = [Source("", "", "", "foo"), Source("", "", "", "bar"), Source("", "", "", "baz")]
        self.assertEqual(p.collate_words(m, s).get_list(), [])

    def test_converts_to_lowercase(self):
        p = Parser()
        m = Meme("all your * -base")
        s = [Source("", "", "", "ALL YOUR DATA")]
        self.assertEqual(p.collate_words(m, s).get_list(), [("data",1)])
        
if __name__ == "__main__":
    unittest.main()
