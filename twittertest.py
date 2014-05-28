import unittest
import mock
from twitter import Twitter
from meme import Meme
import os
from secrets import Secrets
from source import Source

class TwitterTest(unittest.TestCase):

    def test_generates_valid_search(self):
        t = Twitter()
        m = Meme("all your * -base")
        self.assertEqual(t._format_query(m), "?q=%22all+your+%2A%22+-base")

    def test_generates_valid_weird_search(self):
        t = Twitter()
        m = Meme("amn't foo-bar * -base")
        self.assertEqual(t._format_query(m), "?q=%22amn%27t+foo-bar+%2A%22+-base")
  
    @mock.patch('TwitterSearch.TwitterSearch')
    def test_gets_sources(self, mock_ts):
        mock_ts.return_value.searchTweets.return_value = {'content': {'statuses': [{'text': 'all your data', 'id_str': '471774952379932673', 'user': {'name': 'bob'}},{'text': 'all your data', 'id_str': '471774952379932673', 'user': {'name': 'bob'}},{'text': 'all your data', 'id_str': '471774952379932673', 'user': {'name': 'bob'}} ]}}
        t = Twitter()
        m = Meme("all your * -base")
        self.assertGreater(len(t.get_sources(m, 3)), 0)
    
    @mock.patch('TwitterSearch.TwitterSearch')
    def test_sources_have_content(self, mock_ts):
        mock_ts.return_value.searchTweets.return_value = {'content': {'statuses': [{'text': 'all your data', 'id_str': '471774952379932673', 'user': {'name': 'bob'}},{'text': 'all your data', 'id_str': '471774952379932673', 'user': {'name': 'bob'}},{'text': 'all your data', 'id_str': '471774952379932673', 'user': {'name': 'bob'}} ]}}
        t = Twitter()
        m = Meme("all your * -base")
        s = t.get_sources(m, 3).pop()
        self.assertNotEqual(s.handle, "")
        self.assertNotEqual(s.text, "")
        self.assertNotEqual(s.link, "")

    @unittest.skip("not logging to file, might use syslog later. Needs mocking")
    def test_should_log_query(self):
        t = Twitter()
        m = Meme("all your * -base")
        old_file_size = os.stat('queries.log').st_size
        t.get_sources(m,3)
        self.assertGreater(os.stat('queries.log').st_size, old_file_size)
    
    @unittest.skip("not logging to file, might use syslog later. Needs mocking")
    def test_should_log_twitter_exception(self):
        t = Twitter()
        m = Meme("all your * -base")
        old_file_size = os.stat('errors.log').st_size
        old_secret = Secrets.access_token_secret
        Secrets.access_token_secret = "wrong secret"
        t.get_sources(m,3)
        self.assertGreater(os.stat('errors.log').st_size, old_file_size)
        Secrets.access_token_secret = old_secret #hmm, smells bad. Tests might not run in order

if __name__ == "__main__":
    unittest.main()
