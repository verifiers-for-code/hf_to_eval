def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    

    Action Plan:
    1. Check if the input date string is not empty.
    2. Split the input date string into month, day, and year components using the '-' delimiter.
    3. Convert the month, day, and year components to integers.
    4. Validate the month:
       a. Check if the month is within the range 1-12.
       b. If not, return False.
    5. Validate the day based on the month:
       a. For months 1, 3, 5, 7, 8, 10, 12, check if the day is within the range 1-31.
       b. For months 4, 6, 9, 11, check if the day is within the range 1-30.
       c. For month 2, check if the day is within the range 1-29.
       d. If the day is invalid for the month, return False.
    6. If any of the above steps raise an exception (e.g., invalid input format), return False.
    7. If all validation steps pass, return True, indicating a valid date."""

    # Check if the input date string is not empty
    if not date:
        return False

    # Split the input date string into month, day, and year components using the '-' delimiter
    try:
        month, day, year = date.split('-')
    except ValueError:
        return False

    # Convert the month, day, and year components to integers
    try:
        month = int(month)
        day = int(day)
        year = int(year)
    except ValueError:
        return False

    # Validate the month
    if month < 1 or month > 12:
        return False

    # Validate the day based on the month
    if month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31):
        return False
    elif month in [4, 6, 9, 11] and (day < 1 or day > 30):
        return False
    elif month == 2 and (day < 1 or day > 29):
        return False

    return True