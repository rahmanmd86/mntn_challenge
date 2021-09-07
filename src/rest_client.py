from src.validators import Validators
import requests, logging, json
from src.validators import Validators

logging.basicConfig(filename='test_result.log', encoding='utf-8')
logger = logging.getLogger(__name__)

class RestClient():
    def __init__(self, config) -> None:
        self.url = config['base_url']
        self.headers = config['headers']
        self.response = None
        self.data = None

    """
    Placeholder method to improve test verbosity
    """
    def sends(self):
        return self

    """
    Associates response object to the class
    """
    def sees(self, response={}):
        self.response = response
        return self

    def body(self):
        self.data = self.response.json()
        return self

    # Requests

    """
    Calls GET method for a resource
    """
    def get_request(self, path, params={}):
        self.response = requests.get(f'{self.url}{path}', params=params, headers=self.headers)
        return self.response

    """
    Calls POST method for a resource
    """
    def post_request(self, path, body={}, params={}):
        self.response = requests.post(f'{self.url}{path}', data=json.dumps(body), params=params, headers=self.headers)
        return self.response

    """
    Calls PUT method for a resource
    """
    def put_request(self, path, body={}, params={}):
        self.response = requests.put(f'{self.url}{path}', data=json.dumps(body), params=params, headers=self.headers)
        return self.response

    """
    Calls DELETE method for a resource
    """
    def delete_request(self, path, params={}):
        self.response = requests.delete(f'{self.url}{path}', params=params, headers=self.headers)
        return self.response

    # Validations    

    """
    Asserts response status code
    """
    # def status_code(self, code=None):
    #     super().validate(code, self.response.status_code)
    
    # def matches_schema(self, filename):
    #     super().assert_valid_schema(self.data, filename)

    # def size(self, length):
    #     super().validate(length, len(self.data))

    # def contains(self, expected=None):
    #     super().validate(expected, self.data)

    # def as_empty(self):
    #     empty = [{},[],""]
    #     try:
    #         assert self.data in empty
    #     except:
    #         logger.error(f'Expected: None, Actual: {self.data}')
    #         raise Exception("Test case failed")

