from math import sqrt

class Parser:
    def __init__(self, start = 0, end = 100):
        self.range = range(start, end + 1)

    def is_multiple_of(self, n, x):
        return x % n == 0

    def is_fibonacci(self, n):
        if n == 0:
            return True

        lower_condition = self.is_multiple_of(1, sqrt(5*n**2 - 4))
        upper_condition = self.is_multiple_of(1, sqrt(5*n**2 + 4))
        return lower_condition or upper_condition

    def int_to_phrase(self, n):
        if n == 0:
            return "Flamingo"

        is_multiple_of_three = self.is_multiple_of(3, n)
        is_multiple_of_five = self.is_multiple_of(5, n)
        is_fibonacci = self.is_fibonacci(n)

        if is_multiple_of_three and is_multiple_of_five and is_fibonacci:
            return "Pink Flamingo"
        if is_fibonacci:
            return "Flamingo"
        if is_multiple_of_three and is_multiple_of_five:
            return "FizzBuzz"
        if is_multiple_of_five:
            return "Buzz"
        if is_multiple_of_three:
            return "Fizz"
        
        return str(n)

    def generate_output(self):
        sequence = [self.int_to_phrase(n) for n in self.range]
        return ', '.join(sequence)
