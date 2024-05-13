from lambda_function import lambda_handler

def test_lambda_handler_invalid_params_1():
    event = {
        'day': '1',
        'month': '1',
    }
    context = {}

    # Invoke the Lambda function
    response = lambda_handler(event, context)

    # Check if the response status code is 400
    assert response["statusCode"] == 400
    assert 'Error, at least one parameter is missing' in response['body']

def test_lambda_handler_invalid_params_2():
    event = {
        'day': 'aaaaaaa',
        'month': '3ru',
        'year': '%$!&$%&'
    }
    context = {}

    # Invoke the Lambda function
    response = lambda_handler(event, context)

    # Check if the response status code is 400
    assert response["statusCode"] == 400
    assert 'in a valid format' in response['body']

def test_lambda_handler_valid_age():
    event = {
        'day': '1',
        'month': '1',
        'year': '2000'
    }
    context = {}

    # Invoke the Lambda function
    response = lambda_handler(event, context)

    # Check if the response status code is 200
    assert response["statusCode"] == 200
    assert 'Your access to the casino was approved' in response['body']

def test_lambda_handler_invalid_age():
    event = {
        'day': '1',
        'month': '1',
        'year': '9000'
    }
    context = {}

    # Invoke the Lambda function
    response = lambda_handler(event, context)

    # Check if the response status code is 200
    assert response["statusCode"] == 200
    assert 'please try another day' in response['body']
