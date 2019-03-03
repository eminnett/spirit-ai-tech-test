import pytest
import json
import urllib
import web_api

@pytest.fixture
def client():
    web_api.app.config['TESTING'] = True
    client = web_api.app.test_client()
    yield client

api_route = '/api/v1.0'
fizzbuzz_route = api_route + '/fizzbuzz-with-a-pink-flamingo'
roman_numeral_calculator_route = api_route + '/roman-numeral/calculator/?expression='

def test_root_request(client):
    response = client.get('/')
    assert b'Please use the appropriate API route for your request.' in response.data


def test_fizzbuzz_with_a_pink_flamingo_with_defaults(client):
    data = parse_response(client.get(fizzbuzz_route))
    assert len(data) == 101
    assert data[:5] == ["Flamingo", "Flamingo", "Flamingo", "Flamingo", "4"]
    assert data[-5:] == ["Fizz", "97", "98", "Fizz", "Buzz"]


def test_fizzbuzz_with_a_pink_flamingo_with_start(client):
    data = parse_response(client.get(fizzbuzz_route + '/90'))
    assert data == ['FizzBuzz', '91', '92', 'Fizz', '94', 'Buzz', 'Fizz', '97', '98', 'Fizz', 'Buzz']

    data = parse_response(client.get(fizzbuzz_route + '/110'))
    assert data == ['Buzz', '101', 'Fizz', '103', '104', 'FizzBuzz', '106', '107', 'Fizz', '109', 'Buzz']


def test_fizzbuzz_with_a_pink_flamingo_with_start_and_end(client):
    data = parse_response(client.get(fizzbuzz_route + '/5/10'))
    assert data == ['Flamingo', 'Fizz', '7', 'Flamingo', 'Fizz', 'Buzz']

    data = parse_response(client.get(fizzbuzz_route + '/5/0'))
    assert data == ['Flamingo', 'Flamingo', 'Flamingo', 'Flamingo', '4', 'Flamingo']

    data = parse_response(client.get(fizzbuzz_route + '/6760/6770'))
    assert data == ['Buzz', '6761', 'Fizz', '6763', '6764', 'Pink Flamingo', '6766', '6767', 'Fizz', '6769', 'Buzz']


def test_roman_numeral_calculator(client):
    expression = '(V + IX) * III'
    response = client.get(roman_numeral_calculator_route + urllib.parse.quote(expression))
    data = parse_response(response)
    assert data == {'expression': expression, 'result': 'XLII'}


def test_roman_numeral_calculator_with_unevaluatable_expression(client):
    expression = '((V + IV)'
    response = client.get(roman_numeral_calculator_route + urllib.parse.quote_plus(expression))
    data = parse_response(response)
    error_message = 'The roman numeral calculator can only process expressions with evaluatable syntax.'
    assert response.status == '422 UNPROCESSABLE ENTITY'
    assert data == {'expression': expression, 'error': error_message}


def test_roman_numeral_calculator_with_non_integer_result(client):
    expression = 'V / IV'
    response = client.get(roman_numeral_calculator_route + urllib.parse.quote_plus(expression))
    data = parse_response(response)
    error_message = 'The roman numeral calculator can only process expressions that evaluate to an integer.'
    assert response.status == '422 UNPROCESSABLE ENTITY'
    assert data == {'expression': expression, 'error': error_message}


def test_roman_numeral_calculator_with_missing_expression(client):
    response = client.get(roman_numeral_calculator_route)
    data = parse_response(response)
    error_message = 'An expression must be provided via the request query string using the "expression" key.'
    assert response.status == '422 UNPROCESSABLE ENTITY'
    assert data == {'error': error_message}

def parse_response(response):
    return json.loads(response.get_data(as_text=True))