import json
import numpy as np

def lambda_handler(event, context):
    # TODO implement the logic
    random_int = np.random.randint(10**6, size=2)[0]
    return {
        'statusCode': 200,
        'body': json.dumps('The random number generated was ' + str(random_int))
    }
