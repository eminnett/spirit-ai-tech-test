# Response to Task 1

The 'FizzBuzz with a Pink Flamingo' program is a simple Python program that prints the output string
to the terminal when executed.

The program can be executed by running `python fizz_buzz_with_a_pink_flamingo` from the project root or `python .` from inside the `fizz_buzz_with_a_pink_flamingo` directory.

The program defaults to a range of 0 to 100 (inclusive) but takes optional arguments to modify this range. If one argument is given, it is the start of the range when less than 100 and the end when greater. When two arguments are given, the smaller number is the start of the range and the larger number is the end.

These are a few examples of how this can be used:
```
$ > python fizz_buzz_with_a_pink_flamingo 5 10
Flamingo, Fizz, 7, Flamingo, Fizz, Buzz

$ > python fizz_buzz_with_a_pink_flamingo 5 10
Flamingo, Flamingo, Flamingo, Flamingo, 4, Flamingo

$ > python fizz_buzz_with_a_pink_flamingo 105
Buzz, 101, Fizz, 103, 104, FizzBuzz

$ > python fizz_buzz_with_a_pink_flamingo 6760 6770
Buzz, 6761, Fizz, 6763, 6764, Pink Flamingo, 6766, 6767, Fizz, 6769, Buzz
```

# Response to Task 2

The Roman Numeral Calculator program is comprised of two Ruby modules `RomanNumeral::Converter` and 
`RomanNumeral::Converter` and `RomanNumeral::Calculator`. The converter handles the conversion of
roman numerals to integers and vice versa while the calculator handles the evaluation of mathematical
expressions that use roman numerals instead of arabic numerals.

These modules can be used as follows:
```
IRB > RomanNumeral::Converter.to_integer('IX')
9

IRB > RomanNumeral::Converter.to_roman_numeral(19)
'XIX'

IRB > RomanNumeral::Calculator.evaluate('(V + IX) * III')
'XLII'
```

The calculator can also be used used from the terminal. This example assumes the current working director is inside the `roman_numeral_calculator` folder.
```
$ > ruby roman_numeral_calculator.rb "VI / II + IX * III" 
XXX
```