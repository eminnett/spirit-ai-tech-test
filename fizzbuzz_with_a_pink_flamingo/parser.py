"""The FizzBuzz with a Pink Flamingo Parser"""
from math import sqrt

class Parser:
    """
    Generates the FizzBuzz with a Pink Flamingo for a given range (0-100 inclusive by default).
    """
    def __init__(self, start=0, end=100):
        self.range = range(start, end + 1)

    @staticmethod
    def is_multiple_of(base, num):
        """Is num a multiple of base?"""
        return num % base == 0

    def is_fibonacci(self, num):
        """Is num a member of the Fibonacci sequence?"""
        if num == 0:
            return True

        lower_condition = self.is_multiple_of(1, sqrt(5*num**2 - 4))
        upper_condition = self.is_multiple_of(1, sqrt(5*num**2 + 4))
        return lower_condition or upper_condition

    def int_to_phrase(self, num):
        """Convert num into the correct FizzBuzz word or phrase."""
        if num == 0:
            return "Flamingo"

        is_multiple_of_three = self.is_multiple_of(3, num)
        is_multiple_of_five = self.is_multiple_of(5, num)
        is_fibonacci = self.is_fibonacci(num)

        result = str(num)

        if is_multiple_of_three and is_multiple_of_five and is_fibonacci:
            result = "Pink Flamingo"
        elif is_fibonacci:
            result = "Flamingo"
        elif is_multiple_of_three and is_multiple_of_five:
            result = "FizzBuzz"
        elif is_multiple_of_five:
            result = "Buzz"
        elif is_multiple_of_three:
            result = "Fizz"

        return result

    def generate_output(self):
        """Generate the FizzBuzz output for the parser range."""
        sequence = [self.int_to_phrase(n) for n in self.range]
        return ', '.join(sequence)

    def print_output(self):
        """nodoc"""
        print(self.generate_output())
