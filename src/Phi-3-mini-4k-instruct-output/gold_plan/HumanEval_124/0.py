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
    1. Implement error handling to catch any exceptions during the validation process.
    2. Remove any leading or trailing whitespace from the input date string.
    3. Split the date string into month, day, and year components using the '-' separator.
    4. Convert the month, day, and year components to integers.
    5. Check if the month is valid (between 1 and 12).
    6. Create lists of months with 31 days and 30 days.
    7. Check the day validity based on the month:
       - For months with 31 days, check if the day is between 1 and 31.
       - For months with 30 days, check if the day is between 1 and 30.
       - For February (month 2), check if the day is between 1 and 29.
    8. If any check fails, return False.
    9. If all checks pass, return True.
    10. If any exception occurs during the process, return False.
    """
    try:
        date = date.strip()
        month, day, year = map(int, date.split('-'))

        if month < 1 or month > 12:
            return False

        if month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31):
            return False

        if month in [4, 6, 9, 11] and (day < 1 or day > 30):
            return False

        if month == 2 and (day < 1 or day > 29):
            return False

        return True
    except Exception:
        return False