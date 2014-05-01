import unittest
from twitter import Twitter
from meme import Meme
import os
from secrets import Secrets

class TwitterTest(unittest.TestCase):

    def test_generates_valid_search(self):
        t = Twitter()
        m = Meme("all your * -base")
        self.assertEqual(t._format_query(m), "?q=%22all+your+%2A%22+-base")

    def test_gets_texts(self):
        t = Twitter()
        m = Meme("all your * -base")
        self.assertEqual(len(t.get_texts(m, 3)), 3)

    def test_should_log_query(self):
        t = Twitter()
        m = Meme("all your * -base")
        old_file_size = os.stat('queries.log').st_size
        t.get_texts(m,3)
        self.assertGreater(os.stat('queries.log').st_size, old_file_size)

    def test_should_log_twitter_exception(self):
        t = Twitter()
        m = Meme("all your * -base")
        old_file_size = os.stat('errors.log').st_size
        Secrets.access_token_secret = "wrong secret"
        t.get_texts(m,3)
        self.assertGreater(os.stat('errors.log').st_size, old_file_size)

if __name__ == "__main__":
    unittest.main()
