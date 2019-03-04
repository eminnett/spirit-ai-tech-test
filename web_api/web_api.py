#!flask/bin/python
"""The Web API"""
import subprocess
import re
from flask import Flask, request, jsonify

app = Flask(__name__) # pylint: disable=invalid-name

API_ROUTE = '/api/v1.0'
FIZZBUZZ_PROGRAM = '../fizzbuzz_with_a_pink_flamingo/__main__.py'
RN_CALCULATOR_PROGRAM = '../roman_numeral_calculator/roman_numeral_calculator.rb'
FIZZBUZZ_ROUTE = API_ROUTE + '/fizzbuzz-with-a-pink-flamingo'
ROMAN_NUMERAL_ROUTE = API_ROUTE + '/roman-numeral'

@app.route('/')
def index():
    """nodoc"""
    return "Please use the appropriate API route for your request."

@app.route(FIZZBUZZ_ROUTE, methods=['GET'], defaults={'start': 0, 'end': 100})
@app.route(FIZZBUZZ_ROUTE + '/<int:start>', methods=['GET'], defaults={'end': 100})
@app.route(FIZZBUZZ_ROUTE + '/<int:start>/<int:end>', methods=['GET'])
def fizzbuzz_with_a_pink_flamingo(start, end):
    """Get the results of the fizzbuzz_with_a_pink_flamingo program."""
    process_params = ['python', FIZZBUZZ_PROGRAM, str(start), str(end)]
    process = subprocess.Popen(process_params, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out, err = process.communicate()
    results = []
    if err is None:
        results = parse_program_output(out).split(', ')
    return jsonify(results)

@app.route(ROMAN_NUMERAL_ROUTE + '/calculator/', methods=['GET'])
def roman_numeral_calculator():
    """
    Get the result of evaluating the query string expression using the
    roman_numeral_calculator program.
    """
    expression = request.args['expression']
    if expression is None or expression == '':
        error_message = 'An expression must be provided via the request query string using the "expression" key.'
        return jsonify({'error': error_message}), 422

    process_params = ['ruby', RN_CALCULATOR_PROGRAM, expression]
    process = subprocess.Popen(process_params, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out, err = process.communicate()
    result = {'expression': expression}
    status = 200
    if err is None:
        output = parse_program_output(out)
        if '(ArgumentError)' in output:
            msg = re.findall(r"(\w[\w\s\.]+)\s\(ArgumentError\)", output)[0]
            result['error'] = msg
            status = 422
        else:
            result['result'] = parse_program_output(out)

    return jsonify(result), status

def parse_program_output(output):
    """Extract the string from the program output"""
    return str(output).replace("b'", '').replace("\\n'", '')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
