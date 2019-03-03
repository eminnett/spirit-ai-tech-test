# pylint: disable=redefined-outer-name
# pylint: disable=invalid-name
"""Web API Automated Tests"""
import json
import urllib
import pytest
import web_api

@pytest.fixture
def client():
    """nodoc"""
    web_api.app.config['TESTING'] = True
    client = web_api.app.test_client()
    yield client

API_ROUTE = '/api/v1.0'
FIZZBUZZ_ROUTE = API_ROUTE + '/fizzbuzz-with-a-pink-flamingo'
ROMAN_NUMERAL_CALCULATOR_ROUTE = API_ROUTE + '/roman-numeral/calculator/?expression='

def test_root_request(client):
    """nodoc"""
    response = client.get('/')
    assert b'Please use the appropriate API route for your request.' in response.data


def test_fizzbuzz_with_a_pink_flamingo_with_defaults(client):
    """Ensure the FizzBuzz endpoint returns the correct response when using default parameters."""
    data = parse_response(client.get(FIZZBUZZ_ROUTE))
    assert len(data) == 101
    assert data[:5] == ["Flamingo", "Flamingo", "Flamingo", "Flamingo", "4"]
    assert data[-5:] == ["Fizz", "97", "98", "Fizz", "Buzz"]


def test_fizzbuzz_with_a_pink_flamingo_with_start(client):
    """Ensure the FizzBuzz endpoint returns the correct response when using one default parameter."""
    data = parse_response(client.get(FIZZBUZZ_ROUTE + '/90'))
    assert data == ['FizzBuzz', '91', '92', 'Fizz', '94', 'Buzz', 'Fizz', '97', '98', 'Fizz', 'Buzz']

    data = parse_response(client.get(FIZZBUZZ_ROUTE + '/110'))
    assert data == ['Buzz', '101', 'Fizz', '103', '104', 'FizzBuzz', '106', '107', 'Fizz', '109', 'Buzz']


def test_fizzbuzz_with_a_pink_flamingo_with_start_and_end(client):
    """Ensure the FizzBuzz endpoint returns the correct response when both parameter are given."""
    data = parse_response(client.get(FIZZBUZZ_ROUTE + '/5/10'))
    assert data == ['Flamingo', 'Fizz', '7', 'Flamingo', 'Fizz', 'Buzz']

    data = parse_response(client.get(FIZZBUZZ_ROUTE + '/5/0'))
    assert data == ['Flamingo', 'Flamingo', 'Flamingo', 'Flamingo', '4', 'Flamingo']

    data = parse_response(client.get(FIZZBUZZ_ROUTE + '/6760/6770'))
    assert data == ['Buzz', '6761', 'Fizz', '6763', '6764', 'Pink Flamingo', '6766', '6767', 'Fizz', '6769', 'Buzz']


def test_roman_numeral_calculator(client):
    """Ensure the roman numeral calculator returns the correct response."""
    expression = '(V + IX) * III'
    response = client.get(ROMAN_NUMERAL_CALCULATOR_ROUTE + urllib.parse.quote(expression))
    data = parse_response(response)
    assert data == {'expression': expression, 'result': 'XLII'}


def test_roman_numeral_calculator_with_unevaluatable_expression(client):
    """Ensure the appropriate error is returned when the expression includes a syntax error."""
    expression = '((V + IV)'
    response = client.get(ROMAN_NUMERAL_CALCULATOR_ROUTE + urllib.parse.quote_plus(expression))
    data = parse_response(response)
    error_message = 'The roman numeral calculator can only process expressions with evaluatable syntax.'
    assert response.status == '422 UNPROCESSABLE ENTITY'
    assert data == {'expression': expression, 'error': error_message}


def test_roman_numeral_calculator_with_non_integer_result(client):
    """Ensure the appropriate error is returned when the expression results in a float."""
    expression = 'V / IV'
    response = client.get(ROMAN_NUMERAL_CALCULATOR_ROUTE + urllib.parse.quote_plus(expression))
    data = parse_response(response)
    error_message = 'The roman numeral calculator can only process expressions that evaluate to an integer.'
    assert response.status == '422 UNPROCESSABLE ENTITY'
    assert data == {'expression': expression, 'error': error_message}


def test_roman_numeral_calculator_with_missing_expression(client):
    """Ensure the appropriate error is returned when the expression is missing."""
    response = client.get(ROMAN_NUMERAL_CALCULATOR_ROUTE)
    data = parse_response(response)
    error_message = 'An expression must be provided via the request query string using the "expression" key.'
    assert response.status == '422 UNPROCESSABLE ENTITY'
    assert data == {'error': error_message}

def parse_response(response):
    """Parse the JSON response so it can be interrogated."""
    return json.loads(response.get_data(as_text=True))
