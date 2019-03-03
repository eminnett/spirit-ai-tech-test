#!flask/bin/python
import subprocess
import re
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Please use the appropriate API route for your request."

api_route = '/api/v1.0'

fizzbuzz_route = api_route + '/fizzbuzz-with-a-pink-flamingo'
@app.route(fizzbuzz_route, methods=['GET'], defaults={'start': 0, 'end': 100})
@app.route(fizzbuzz_route + '/<int:start>', methods=['GET'], defaults={'end': 100})
@app.route(fizzbuzz_route + '/<int:start>/<int:end>', methods=['GET'])
def fizzbuzz_with_a_pink_flamingo(start, end):
    """Get the results of the fizzbuzz_with_a_pink_flamingo program."""
    process_params = ['python', '../fizzbuzz_with_a_pink_flamingo', str(start), str(end)]
    process = subprocess.Popen(process_params, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) 
    out, err = process.communicate()
    results = []
    if err == None:
        results = parse_program_output(out).split(', ')
    return jsonify(results)

roman_numeral_route = api_route + '/roman-numeral'
@app.route(roman_numeral_route + '/calculator/', methods=['GET'])
def roman_numeral_calculator():
    """Get the result of evaluating the query string expression using the roman_numeral_calculator program."""
    expression = request.args['expression']
    if expression == None or expression == '':
        error_message = 'An expression must be provided via the request query string using the "expression" key.'
        return jsonify({'error': error_message}), 422

    process_params = ['ruby', '../roman_numeral_calculator/roman_numeral_calculator.rb', expression]
    process = subprocess.Popen(process_params, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) 
    out, err = process.communicate()
    result = {'expression': expression}
    status = 200
    if err == None:
        output = parse_program_output(out)
        if '(ArgumentError)' in output:
            msg = re.findall("(\w[\w\s\.]+)\s\(ArgumentError\)", output)[0]
            result['error'] = msg
            status = 422
        else:
            result['result'] = parse_program_output(out)
        
    return jsonify(result), status

def parse_program_output(output):
    return str(output).replace("b'", '').replace("\\n'", '')

if __name__ == '__main__':
    app.run(debug=True)