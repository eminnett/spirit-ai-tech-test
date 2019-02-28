import unittest

from .parser import Parser

class ParserTest(unittest.TestCase):
    def test_range(self):
        start = 0
        end = 5
        parser = Parser(start, end)

        self.assertTrue(parser.range == range(start, end + 1))

if __name__ == '__main__':
    unittest.main()