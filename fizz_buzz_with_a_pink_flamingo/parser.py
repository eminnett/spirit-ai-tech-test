class Parser:
    def __init__(self, start = 0, end = 100):
        self.range = range(start, end + 1)

    def is_multiple_of(self, n, x):
        return x % n == 0

    def generate_output(self):
        print("This will ultimately return the parsed FizzBuzz With a Pink Flamingo output.")