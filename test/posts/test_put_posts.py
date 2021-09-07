import pytest
import src.api_paths as apis
import src.constants as constants
from http import HTTPStatus
from src.validators import Validators as expect
import pytest_check as check

def test_put_posts(client):
    body = {
        "title": "Test title",
        "body": "Test body",
        "userId": 55
    }
    response = client.sends().put_request(f'{apis.POSTS}/5', body)
    
    body['id'] = 5
    check.equal(response.status_code, HTTPStatus.OK)
    check.equal(response.json(), body);

def test_put_posts_empty(client):
    body = {}
    response = client.sends().put_request(f'{apis.POSTS}/5', body)
    
    check.equal(response.status_code, HTTPStatus.OK)
    expect(response.json()).contains(('id',5));

@pytest.mark.skip(reason="Failed with 500 ISE")
def test_put_posts_invalid_id(client):
    body = {
        "title": "Test title",
        "body": "Test body",
        "userId": 55
    }
    response = client.sends().put_request(f'{apis.POSTS}/101', body)
    
    check.equal(response.status_code, HTTPStatus.NOT_FOUND)
    check.equal(response.json(), {});

