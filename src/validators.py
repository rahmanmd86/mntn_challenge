import json, logging
from os.path import join, dirname
from jsonschema import validate
import pytest_check as check

logging.basicConfig(filename='test_result.log', encoding='utf-8')
logger = logging.getLogger(__name__)

class Validators:

    def __init__(self, obj) -> None:
        self.obj = obj

    # def status_code(self, code=None):
    #     validate(code, self.response.status_code)

    
    def matches_schema(self, filename):
        self._assert_valid_schema(self.obj, filename)

    # def size(self, length):
    #     validate(length, len(self.data))

    def contains(self, expected):
        self._validate_data(expected, self.obj)
    
    def _assert_valid_schema(self, data, schema_file):
        """ Checks whether the given data matches the schema """

        schema = self._load_json_schema(schema_file)
        return validate(data, schema)

    def _validate_data(self, expected, actual):
        try:
            # if type(actual) not in [list, dict, tuple]:
            #     check.equal(expected,actual)
            if type(actual) == list:
                # if type(expected) == int:
                #     check.equal(expected,actual)
                if len(actual) > 0:
                    for items in actual:
                        self._validate_key_values(expected, items)
            if type(actual) == dict:
                self._validate_key_values(expected, actual)

            
        except:
            logger.error(f'Expected: {expected}, Actual: {actual}')
            raise Exception("Test case failed")

    def _load_json_schema(self, filename):
        """ Loads the given schema file """

        relative_path = join('schemas', filename)
        absolute_path = join(dirname(__file__), relative_path)

        with open(absolute_path) as schema_file:
            return json.loads(schema_file.read())

    def _validate_key_values(self, expected, actual):
        if type(expected) == str:
            check.is_in(expected, actual)
        elif type(expected) == tuple:
            check.is_in(expected, actual.items())