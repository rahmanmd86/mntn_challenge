# mntn_challenge [https://mountain.com/]

# Assessment Guidelines

- No postman scripts
- No soapui
- No record/play
- Code must be turned in and executable (no copy/paste, no screenshots, ...)
- You can link to github repo, if available

For the assessment, please choose a public API to automate and provide the following:
 - Executable automation you have written to verify the public API
 - Explanation of your approach
 - Pros and cons of approach

# Solution

This repo contains the test framework and the tests as part of the solution for the mntn offline challenge

The API that has been used is defined here https://jsonplaceholder.typicode.com/guide

Sample endpoints for which tests are added

- GET https://jsonplaceholder.typicode.com/posts
- POST https://jsonplaceholder.typicode.com/posts
- PUT https://jsonplaceholder.typicode.com/posts/{postId}
- DELETE https://jsonplaceholder.typicode.com/posts/{postId}

## Getting started

## Prerequisites
- python = 3.9
- pip
- pipenv

## Project Structure

```
mntn_challenge
    |-- src
        |-- schemas
                |-- get_posts_all_response_schema.json
                |-- get_posts_response_schema.json
        |-- api_paths.py
        |-- config.json
        |-- constants.py
        |-- validators.py
        |-- rest_client.py
        |-- helper.py
    |-- tests
        |-- posts
            |-- test_get_posts.py
            |-- test_post_posts.py
            |-- test_put_posts.py
            |-- test_delete_posts.py
    |-- Pipfile
    |-- Pipfile.lock
    |-- conftest.py
    |-- .gitignore
```

## Running the tests

1. Clone the repo
2. Navigate to `mntn_challenge`
3. Install dependencies by using command 
    - `pipenv install`
4. Launch virtual environenment by using command
    - `pipenv shell`
5. Run the tests by using command
    - `pytest`
6. Tests can be run outside virtual environment using command (Optional)
    - `pipenv run pytest`

- Test reports can be generated as HTML using command
    - `pytest --html=<filename>.html`
- Tests can be run in parallel using command
    -  `pytest -n {NUMCPUS}`

## Not covered

- Load and performance testing is not covered as part of this framework, that will be a separate project effort.
- Enhancements: 
    - Enable logging mechanism for the requests and responses
    - Dockerize and containerize to be able to run across various environments
    - Integrate with CICD
    - Test coverage tracking for test management


### Author: Md Mahbubur Rahman