import sys
from parser import Parser # pylint: disable=no-name-in-module

if 'fizz_buzz_with_a_pink_flamingo' in sys.argv:
    sys.argv.remove('fizz_buzz_with_a_pink_flamingo')

start = 0
end = 100
if len(sys.argv) > 0:
    start = int(sys.argv[0])
if len(sys.argv) > 1:
    end = int(sys.argv[1])

Parser(start, end).generate_output()