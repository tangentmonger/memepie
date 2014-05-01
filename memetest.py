import unittest
from meme import Meme


class MemeTest(unittest.TestCase):

    def test_valid_meme_has_raw_meme(self):
        m = Meme("all your * -base")
        self.assertEqual(m.raw_meme, "all your * -base")
        
    def test_valid_meme_has_body(self):
        m = Meme("all your * -base")
        self.assertEqual(m.get_body(), "all your *")
 
    def test_valid_meme_has_exceptions(self):
        m = Meme("all your * -base")
        self.assertEqual(m.get_exceptions(), "-base")
 
    def test_valid_meme_is_valid(self):
        m = Meme("all your * -base")
        self.assertTrue(m.test_valid())

    def test_invalid_meme_has_raw_meme(self):
        m = Meme("nothing here")
        self.assertEqual(m.raw_meme, "nothing here")

    def test_invalid_meme_is_invalid(self):
        m = Meme("nothing here")
        self.assertFalse(m.test_valid())

    def test_two_stars_is_invalid(self):
        m = Meme("* into *")
        self.assertFalse(m.test_valid())

    def test_invalid_characters(self):
        m = Meme("ok <>\"(){}[]")
        self.assertEqual(m.get_body(), "ok")

    def test_hypen_is_not_exception(self):
        m = Meme("foo-bar -baz")
        self.assertEqual(m.get_body(), "foo-bar")
        self.assertEqual(m.get_exceptions(), "-baz")

    def test_punctuation_is_ok(self):
        m = Meme("amn't,. * -isn't")
        self.assertEqual(m.get_body(), "amn't,. *")
        self.assertEqual(m.get_exceptions(), "-isn't")
    

if __name__ == "__main__":
    unittest.main()
