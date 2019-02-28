from math import sqrt

class Parser:
    def __init__(self, start = 0, end = 100):
        self.range = range(start, end + 1)

    def is_multiple_of(self, n, x):
        return x % n == 0

    def is_fibonacci(self, n):
        lower_condition = self.is_multiple_of(1, sqrt(5*n**2 - 4))
        upper_condition = self.is_multiple_of(1, sqrt(5*n**2 + 4))
        return lower_condition or upper_condition

    def int_to_phrase(self, n):
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
        
        return n

    def generate_output(self):
        print("This will ultimately return the parsed FizzBuzz With a Pink Flamingo output.")