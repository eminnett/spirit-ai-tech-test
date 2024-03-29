"""Parser Automated Tests"""
import unittest
from .parser import Parser

class ParserTest(unittest.TestCase):
    """Confirm the expected behaviour for the Parser class"""
    def test_range(self):
        """Ensure the parser range is set correctly."""
        start = 0
        end = 5
        parser = Parser(start, end)

        self.assertTrue(parser.range == range(start, end + 1))

    def test_is_multiple_of(self):
        """Parser.is_multiple_of(n, x) should be true when x is a multiple of n."""
        self.assertFalse(Parser.is_multiple_of(3, 5))

        self.assertTrue(Parser.is_multiple_of(3, 3))
        self.assertTrue(Parser.is_multiple_of(3, 6))
        self.assertTrue(Parser.is_multiple_of(3, 120))

    def test_is_fibonacci(self):
        """parser.is_fibonacci(n) should be true when n is a member of the Fibonacci sequence."""
        parser = Parser()

        self.assertTrue(parser.is_fibonacci(0))
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

    def test_int_to_phrase(self):
        """
        parser.int_to_phrase(n) should return 'Flamingo' when n is a member of the Fibonacci
        sequence, 'Fizz' when n is a multiple of 3, 'Buzz' when n is a multiple of 5, 'FizzBuzz'
        when n is both a multiple of 3 and 5, and 'Pink Flamingo' when all three conditions are met.
        """
        parser = Parser()

        self.assertTrue(parser.int_to_phrase(0) == "Flamingo")
        self.assertTrue(parser.int_to_phrase(1) == "Flamingo")
        self.assertTrue(parser.int_to_phrase(2) == "Flamingo")
        self.assertTrue(parser.int_to_phrase(3) == "Flamingo")
        self.assertTrue(parser.int_to_phrase(5) == "Flamingo")
        self.assertTrue(parser.int_to_phrase(6) == "Fizz")
        self.assertTrue(parser.int_to_phrase(7) == "7")
        self.assertTrue(parser.int_to_phrase(9) == "Fizz")
        self.assertTrue(parser.int_to_phrase(10) == "Buzz")
        self.assertTrue(parser.int_to_phrase(11) == "11")
        self.assertTrue(parser.int_to_phrase(15) == "FizzBuzz")
        self.assertTrue(parser.int_to_phrase(6765) == "Pink Flamingo")

    def test_generate_output(self):
        """parser.generate_output() should return a comma seperated string for the given range."""
        parser = Parser(0, 10)
        expectated_output = ' '.join([
            "Flamingo, Flamingo, Flamingo, Flamingo, 4, Flamingo,",
            "Fizz, 7, Flamingo, Fizz, Buzz"
        ])
        self.assertTrue(parser.generate_output() == expectated_output)

if __name__ == '__main__':
    unittest.main()
