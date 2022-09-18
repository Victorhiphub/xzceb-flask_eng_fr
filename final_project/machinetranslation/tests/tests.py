import unittest

from translator import frenchToEnglish, englishToFrench

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("hello"),"Bonjour")
        self.assertEqual(englishToFrench("welcome"),"Bienvenue")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("bonjour"),"Hello")
        self.assertEqual(frenchToEnglish("bienvenue"),"Welcome")

unittest.main()