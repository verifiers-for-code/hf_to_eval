import re

def valid_date(date):
    """Validates a given date string and returns True if the date is valid, otherwise False."""
    # Step 1: Validate the format of the date string
    if not re.match(r'\d{2}-\d{2}-\d{4}', date):
        return False

    # Step 2: Extract month, day, and year components
    month, day, year = map(int, date.split('-'))

    # Step 3: Validate each part of the date
    if not (1 <= month <= 12):
        return False
    if not (1 <= day <= 31):
        return False

    # Adjust day count for February (28 or 29)
    if month == 2:
        if day > 29:
            return False
        if day == 29 and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            return False

    # Validate days based on month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    else:
        if day < 1 or day > 29:
            return False

    return True