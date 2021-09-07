import json, os

def json_parser(filepath):
    result = None
    if os.path.exists(filepath):
        with open(filepath, 'r') as json_file:
            result = json.load(json_file)

    return result

def filter_response(response, key, value):
    return list(filter(lambda resp: resp[key] == value, response))

