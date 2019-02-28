import unittest

from .parser import Parser

class ParserTest(unittest.TestCase):
    def test_range(self):
        start = 0
        end = 5
        parser = Parser(start, end)

        self.assertTrue(parser.range == range(start, end + 1))
    
    def test_is_multiple_of(self):
        parser = Parser()

        self.assertFalse(parser.is_multiple_of(3, 5))

        self.assertTrue(parser.is_multiple_of(3, 3))
        self.assertTrue(parser.is_multiple_of(3, 6))
        self.assertTrue(parser.is_multiple_of(3, 120))

if __name__ == '__main__':
    unittest.main()