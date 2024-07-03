import datetime

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
    1. Check if the input date string is empty:
        - If empty, return False
    
    2. Split the date string into month, day, and year components:
        - Use the split method to separate the string by the '-' delimiter
        - Store the components in separate variables
    
    3. Validate the date format:
        - Check if the month, day, and year components are in the correct format (e.g.,'mm-dd-yyyy')
        - If not, return False
    
    4. Validate the month and day values:
        - Check if the month is between 1 and 12
        - Check if the day is between 1 and 31, considering the number of days in each month
        - If the month is February, check if the day is between 1 and 29, considering leap years
    
    5. Return the result:
        - If all validations pass, return True
        - If any validation fails, return False
    
    Note: Consider using the datetime module to simplify the date validation process.
    Be careful when handling leap years and the number of days in each month."""

    if not date:
        return False

    try:
        month, day, year = map(int, date.split('-'))
    except ValueError:
        return False

    if not (1 <= month <= 12):
        return False

    if month in [1, 3, 5, 7, 8, 10, 12] and not (1 <= day <= 31):
        return False

    if month in [4, 6, 9, 11] and not (1 <= day <= 30):
        return False

    if month == 2:
        if not (1 <= day <= 29):
            return False
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if not (1 <= day <= 29):
                return False
        else:
            if not (1 <= day <= 28):
                return False

    return True