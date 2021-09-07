import src.api_paths as apis
import src.constants as constants
from http import HTTPStatus
from src.validators import Validators as expect
import pytest_check as check

def test_post_posts(client):
    body = {
        "title": "Test title",
        "body": "Test body",
        "userId": 55
    }
    response = client.sends().post_request(apis.POSTS, body)
    
    body['id'] = 101

    check.equal(response.status_code, HTTPStatus.CREATED)
    check.equal(response.json(), body);

def test_post_posts_empty(client):
    body = {}
    response = client.sends().post_request(apis.POSTS, body)
    
    check.equal(response.status_code, HTTPStatus.CREATED)
    expect(response.json()).contains(('id',101));

# Important: resource will not be really updated on the server but it will be faked as if.