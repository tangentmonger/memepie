import unittest
from source import Source

class SourceTest(unittest.TestCase):

    def test_stores_handle_id(self):
        s = Source("handle_id", "", "", "")
        self.assertEqual(s.handle_id, "handle_id")
    
    def test_stores_handle_text(self):
        s = Source("", "handle", "", "")
        self.assertEqual(s.handle_text, "handle")

    def test_stores_status_id(self):
        s = Source("", "", "1234567890", "")
        self.assertEqual(s.status_id, "1234567890")
    
    def test_stores_status_text(self):
        s = Source("", "", "", "what they twote")
        self.assertEqual(s.status_text, "what they twote")

if __name__ == "__main__":
    unittest.main()

