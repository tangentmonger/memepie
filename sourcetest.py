import unittest
from source import Source

class SourceTest(unittest.TestCase):

    def test_stores_handle(self):
        s = Source("handle", "", "")
        self.assertEqual(s.handle, "handle")

    def test_stores_handle(self):
        s = Source("", "what they twote", "")
        self.assertEqual(s.text, "what they twote")
    
    def test_stores_handle(self):
        s = Source("", "", "twitter.com/linktotweet")
        self.assertEqual(s.link, "twitter.com/linktotweet")

if __name__ == "__main__":
    unittest.main()

