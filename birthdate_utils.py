from datetime import datetime

KEYS_LIST = ['day', 'month', 'year']

def isBirthdateValid(year: int, month: int, day: int) -> bool:
    # Get today's date
    today = datetime.now().date()

    # Calculate the birthdate based on the input parameters
    birthdate = datetime(year, month, day).date()

    # Calculate the age
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    # Check if the age is at least 21
    return age >= 21

def isRequestValid(event):
    for key in KEYS_LIST:
        if key not in event:
            return False
    return True
