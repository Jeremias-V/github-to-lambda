import json
from birthdate_utils import isRequestValid, isBirthdateValid

def lambda_handler(event, context):

    response = {}

    if not isRequestValid(event):
        response['body'] = json.dumps('Error, at least one parameter is missing (day, month, year).')
        response['statusCode'] = 400
        return response
    
    try:

        day = int(event['day'])
        month = int(event['month'])
        year = int(event['year'])

        if isBirthdateValid(year, month, day):
            response['body'] = json.dumps('Welcome! Your access to the casino was approved!')
        else:
            response['body'] = json.dumps('Sorry, you\'re not allowed to enter the casino, please try another day...')

        response['statusCode'] = 200

    except:

        response['body'] = json.dumps('An error has ocurred, make sure to include the day, month and year of the birthdate in a valid format.')
        response['statusCode'] = 400

    return response
