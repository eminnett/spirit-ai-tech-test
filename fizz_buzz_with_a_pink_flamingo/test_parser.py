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

    def test_is_fibonacci(self):
        parser = Parser()

        self.assertTrue(parser.is_fibonacci(1))
        self.assertTrue(parser.is_fibonacci(2))
        self.assertTrue(parser.is_fibonacci(3))
        self.assertTrue(parser.is_fibonacci(5))
        self.assertTrue(parser.is_fibonacci(8))
        self.assertTrue(parser.is_fibonacci(13))
        self.assertTrue(parser.is_fibonacci(21))

        self.assertFalse(parser.is_fibonacci(4))
        self.assertFalse(parser.is_fibonacci(6))
        self.assertFalse(parser.is_fibonacci(7))
        self.assertFalse(parser.is_fibonacci(9))
        self.assertFalse(parser.is_fibonacci(10))

        

if __name__ == '__main__':
    unittest.main()