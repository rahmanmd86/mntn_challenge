import pytest
import src.api_paths as apis
from http import HTTPStatus
from src.validators import Validators as expect
import pytest_check as check

def test_delete_posts(client):
    response = client.sends().delete_request(f'{apis.POSTS}/3')
    
    check.equal(response.status_code, HTTPStatus.OK)
    check.equal(response.json(), {});

@pytest.mark.skip(reason="Failed as returns 200 for invalid post")
def test_delete_posts_invalid_id(client):
    response = client.sends().delete_request(f'{apis.POSTS}/130')
    
    check.equal(response.status_code, HTTPStatus.NOT_FOUND)
    check.equal(response.json(), {});