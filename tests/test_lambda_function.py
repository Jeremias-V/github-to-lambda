from lamba_function import lambda_handler

def test_lambda_handler():
# Event and Context are not used in this example
    event = {}
    context = {}

    # Invoke the Lambda function
    response = lambda_handler(event, context)

    # Check if the S3 object was created successfully
    assert response["statusCode"] == 200