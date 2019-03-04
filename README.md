# Setup

The project has been wrapped in a Docker container. All of the commands in this document assume the following two commands have been executed first.

```
$ > docker build --tag=spirit_ai_tech_test .
$ > docker run -d -p 5000:5000 --name spirit_ai_tech_test spirit_ai_tech_test 
```

The working directory inside the Docker cintainer is `web_api`. The commands in this document reflect this. 

When finsihed, these commands will tidy up the container.

```
$ > docker stop spirit_ai_tech_test
$ > docker rm spirit_ai_tech_test
```

# Response to Task 1

The 'FizzBuzz with a Pink Flamingo' program is a simple Python program that prints the output string
to the terminal when executed.

The program can be executed by running `python fizzbuzz_with_a_pink_flamingo` from the project root or `python .` from inside the `fizzbuzz_with_a_pink_flamingo` directory.

The program defaults to a range of 0 to 100 (inclusive) but takes optional arguments to modify this range. If one argument is given, it is the start of the range when less than 100 and the end when greater. When two arguments are given, the smaller number is the start of the range and the larger number is the end.

These are a few examples of how this can be used:
```
$ > docker exec spirit_ai_tech_test python ../fizzbuzz_with_a_pink_flamingo 5 10
Flamingo, Fizz, 7, Flamingo, Fizz, Buzz

$ > docker exec spirit_ai_tech_test python ../fizzbuzz_with_a_pink_flamingo 5 0
Flamingo, Flamingo, Flamingo, Flamingo, 4, Flamingo

$ > docker exec spirit_ai_tech_test python ../fizzbuzz_with_a_pink_flamingo 105
Buzz, 101, Fizz, 103, 104, FizzBuzz

$ > docker exec spirit_ai_tech_test python ../fizzbuzz_with_a_pink_flamingo 6760 6770
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
$ > docker exec spirit_ai_tech_test ruby ../roman_numeral_calculator/roman_numeral_calculator.rb "VI / II + IX * III" 
XXX
```

# Response to Task 3

The programs from tasks one and two have been wrapped in a simple Flask web API. The server can be run locally by executing `python ./web_api/web_api.py` from the project root directory. The API can then be accessed by making a request to `http://127.0.0.1:5000/`.

The API includes the following routes:
```
'/api/v1.0/fizzbuzz-with-a-pink-flamingo/'
'/api/v1.0/fizzbuzz-with-a-pink-flamingo/0'
'/api/v1.0/fizzbuzz-with-a-pink-flamingo/0/100'
'/api/v1.0/roman-numeral/calculator/?expression=%28V+%2B+IX%29+%2A+III' # This is the encoded version of '(V + IX) * III'
```

The parameters for the `fizzbuzz-with-a-pink-flamingo` are optional with defaults of 0 and 100 just as they are when running the program from the terminal. I wanted to use a RESTful enpoint for the `roman-numeral/calculator/` enpoint but the use of `/` in the expression results in ambiguity when parsing the URL. Using a query string to pass the expression avoids this ambiguity though it does result in inconsistency in how the API is used. Encoding the expression using `urllib.parse` is the only way to ensure the expression is evaluated correctly. Passing the expression as plain text works unless it includes addition. The URL parser in Flask will treat `+` as a space.

The API returns the same results as the two programs as JSON.

# Response to Task 4

There is a good example in my GitHub account of a [sample React application](https://github.com/eminnett/foreign-exchange-explorer) but I don't have an example of Docker usage so I have chosen to go down that route for the fourth task. Networking multiple containers for such a simple project seemed like overkill so I have defined a single docker container to run all of the programs and the Flask web API.

# Testing

All of the test commands can be run in sequence by executing `docker exec spirit_ai_tech_test bash test.sh`.