import pytest
import web_api

@pytest.fixture
def client():
    web_api.app.config['TESTING'] = True
    client = web_api.app.test_client()
    yield client

def test_root_request(client):
    rv = client.get('/')
    assert b'Nothing to see here!' in rv.data