# -*- coding: utf-8 -*-
import unittest
from meme import Meme


class MemeTest(unittest.TestCase):

    def test_valid_meme_has_raw_meme(self):
        m = Meme("all your * -base")
        self.assertEqual(m.raw_meme, "all your * -base")
        
    def test_valid_meme_has_clean_meme(self):
        m = Meme("all your., * -base")
        self.assertEqual(m.get_clean_meme(), "all your * -base")
    
    def test_valid_meme_has_body(self):
        m = Meme("all your * -base")
        self.assertEqual(m.get_body(), "all your *")
 
    def test_valid_meme_has_exceptions(self):
        m = Meme("all your * -base")
        self.assertEqual(m.get_exceptions(), "-base")
 
    def test_valid_meme_is_valid(self):
        m = Meme("all your * -base")
        self.assertTrue(m.is_valid())

    def test_invalid_meme_has_raw_meme(self):
        m = Meme("nothing here")
        self.assertEqual(m.raw_meme, "nothing here")

    def test_invalid_meme_is_invalid(self):
        m = Meme("nothing here")
        self.assertFalse(m.is_valid())
        self.assertEqual(m.get_problem(), "has no wildcard (*)")

    def test_two_stars_is_invalid(self):
        m = Meme("* into *")
        self.assertFalse(m.is_valid())
        self.assertEqual(m.get_problem(), "has too many wildcards (*)")

    def test_invalid_characters(self):
        m = Meme("ok <>\"(){}[],.")
        self.assertEqual(m.get_body(), "ok")

    def test_accents_ok(self):
        m = Meme("milano é *")
        self.assertTrue(m.is_valid)
        self.assertEqual(m.raw_meme, "milano é *")
        self.assertEqual(m.get_body(), "milano é *")

    def test_hypen_is_not_exception(self):
        m = Meme("foo-bar -baz")
        self.assertEqual(m.get_body(), "foo-bar")
        self.assertEqual(m.get_exceptions(), "-baz")

    def test_apostrophe_is_ok(self):
        m = Meme("amn't * -isn't")
        self.assertEqual(m.get_body(), "amn't *")
        self.assertEqual(m.get_exceptions(), "-isn't")
    
    def test_get_parts_valid_1(self):
        m = Meme("* foo")
        self.assertEqual(m.get_parts(), ["", "foo"])

    def test_get_parts_valid_2(self):
        m = Meme("foo *")
        self.assertEqual(m.get_parts(), ["foo", ""])
    
    def test_get_parts_valid_3(self):
        m = Meme("foo * bar")
        self.assertEqual(m.get_parts(), ["foo", "bar"])

if __name__ == "__main__":
    unittest.main()
