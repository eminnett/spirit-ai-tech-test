#!flask/bin/python
import subprocess
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Please use the appropriate API route for your request."

fizzbuzz_route = '/api/v1.0/fizzbuzz-with-a-pink-flamingo'
@app.route(fizzbuzz_route, methods=['GET'], defaults={'start': 0, 'end': 100})
@app.route(fizzbuzz_route + '/<int:start>', methods=['GET'], defaults={'end': 100})
@app.route(fizzbuzz_route + '/<int:start>/<int:end>', methods=['GET'])
def fizzbuzz_with_a_pink_flamingo(start, end):
    process_params = ['python', '../fizzbuzz_with_a_pink_flamingo', str(start), str(end)]
    process = subprocess.Popen(process_params, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) 
    out, err = process.communicate()
    results = []
    if err == None:
        results = str(out).replace("b'", '').replace("\\n'", '').split(', ')
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)