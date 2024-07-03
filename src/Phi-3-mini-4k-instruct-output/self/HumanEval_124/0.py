import re

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
    1. Parse the input date string to validate its format:
        a. Check if the string is in the 'mm-dd-yyyy' format using regex or string methods
    
    2. Extract the month, day, and year components from the date string:
        a. If the format is valid, split the string at the '-' delimiter and parse the resulting parts into integers
    
    3. Validate each part of the date using predefined checks:
        a. If any part is empty, return False
        b. Verify the length of days based on the extracted month:
            - For months 1, 3, 5, 7, 8, 10, 12: days should be within 1-31
            - For months 4, 6, 9, 11: days should be within 1-30
            - For month 2: days should be within 1-29 (considering it's not a leap year)
        c. Return False if any day value is less than 1 or higher than 31 (or the respective max for the month)
    
    4. Return True if all parts are valid"""

    # Step 1: Check the format of the date string
    if not re.match(r'^\d{2}-\d{2}-\d{4}$', date):
        return False

    # Step 2: Extract the month, day, and year components
    month, day, year = map(int, date.split('-'))

    # Step 3: Validate each part of the date
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2 and day > 29:
        return False

    # Step 4: Return True if all parts are valid
    return True