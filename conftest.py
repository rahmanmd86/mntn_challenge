import pytest
from src.helper import json_parser
from src.rest_client import RestClient

@pytest.fixture()
def client():
    url_config = json_parser('src/config.json')
    client = RestClient(url_config)
    yield client
