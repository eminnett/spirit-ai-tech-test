"""The FizzBuzz program"""
import sys
from parser import Parser # pylint: disable=no-name-in-module

def execute_fizz_buzz():
    """nodoc"""
    folder = 'fizzbuzz_with_a_pink_flamingo'
    args = [arg for arg in sys.argv if folder not in arg and arg != '.']

    start = 0
    end = 100
    if len(args) > 0:
        start = int(args[0])
    if len(args) > 1:
        end = int(args[1])

    start, end = min(start, end), max(start, end)

    Parser(start, end).print_output()

execute_fizz_buzz()
