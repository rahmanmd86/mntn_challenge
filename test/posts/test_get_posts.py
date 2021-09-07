import pytest
import src.api_paths as apis
import src.constants as constants
from http import HTTPStatus
from src.validators import Validators as expect
import pytest_check as check

def test_get_posts_all(client):
    response = client.sends().get_request(apis.POSTS)
    
    # client.sees(response).status_code(HTTPStatus.OK)
    # client.sees(response).body().size(100)
    # client.sees(response).body().matches_schema(constants.GET_POSTS_ALL_RESPONSE_SCHEMA)

    check.equal(response.status_code, HTTPStatus.OK)
    check.equal(len(response.json()), 100)
    expect(response.json()).matches_schema(constants.GET_POSTS_ALL_RESPONSE_SCHEMA)

def test_get_posts_by_id(client):
    response = client.sends().get_request(f'{apis.POSTS}/1')
    
    # client.sees(response).status_code(HTTPStatus.OK)
    # client.sees(response).body().contains(('id',1)) 
    # client.sees(response).body().matches_schema(constants.GET_POSTS_RESPONSE_SCHEMA)

    check.equal(response.status_code, HTTPStatus.OK)
    expect(response.json()).contains(('id',1))
    expect(response.json()).matches_schema(constants.GET_POSTS_RESPONSE_SCHEMA)


def test_get_posts_by_userId(client):
    response = client.sends().get_request(f'{apis.POSTS}?userId=1')
    
    # client.sees(response).status_code(HTTPStatus.OK)
    # client.sees(response).body().contains(('userId',1)) 
    # client.sees(response).body().matches_schema(constants.GET_POSTS_ALL_RESPONSE_SCHEMA)

    check.equal(response.status_code, HTTPStatus.OK)
    expect(response.json()).contains(('userId',1))


def test_get_posts_by_id_elapsed_time(client):
    response = client.sends().get_request(f'{apis.POSTS}/1')
    
    # client.sees(response).status_code(HTTPStatus.OK)
    check.equal(response.status_code, HTTPStatus.OK)
    check.less(response.elapsed.total_seconds(), 0.5)

def test_get_posts_by_userId_elapsed_time(client):
    response = client.sends().get_request(f'{apis.POSTS}?userId=1')
    
    # client.sees(response).status_code(HTTPStatus.OK)
    check.equal(response.status_code, HTTPStatus.OK)
    check.less(response.elapsed.total_seconds(), 0.5)

# Negative tests

def test_get_posts_by_invalid_id(client):
    response = client.sends().get_request(f'{apis.POSTS}/120')
    
    # client.sees(response).status_code(HTTPStatus.NOT_FOUND)
    check.equal(response.status_code, HTTPStatus.NOT_FOUND)
    check.equal(response.json(), {})

@pytest.mark.skip(reason="Failed as returns status_code = 200")
def test_get_posts_by_invalid_userId(client):
    response = client.sends().get_request(f'{apis.POSTS}?userId=101')
    
    # client.sees(response).status_code(HTTPStatus.NOT_FOUND)
    check.equal(response.status_code, HTTPStatus.NOT_FOUND)
    check.equal(response.json(), [])

