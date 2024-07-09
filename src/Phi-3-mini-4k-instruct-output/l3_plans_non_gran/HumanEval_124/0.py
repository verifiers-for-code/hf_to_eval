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
    1. Split the input date string into month, day, and year components using the '-' delimiter.
    2. Convert the month, day, and year components to integers.
    3. Validate the date format:
        a. Check if the month, day, and year are integers.
        b. Check if the date string has exactly three components separated by '-'.
    4. Check the day, month, and year ranges:
        a. Validate the day range (1-31) based on the month.
        b. Validate the month range (1-12).
        c. Validate the year range (1-9999).
    5. Handle edge cases and errors:
        a. Raise a ValueError if the date string is empty or has less than three components.
        b. Raise a ValueError if the day, month, or year is not an integer.
        c. Raise a ValueError if the date string is in an invalid format.
    6. Return True if the date is valid, False otherwise."""

    # Step 1: Split the input date string into month, day, and year components using the '-' delimiter.
    try:
        month, day, year = date.split('-')
    except ValueError:
        raise ValueError("Invalid date format. The date should be in the format: mm-dd-yyyy")

    # Step 2: Convert the month, day, and year components to integers.
    try:
        month = int(month)
        day = int(day)
        year = int(year)
    except ValueError:
        raise ValueError("Invalid date format. The date should be in the format: mm-dd-yyyy")

    # Step 3: Validate the date format.
    if len(date.split('-')) != 3:
        raise ValueError("Invalid date format. The date should be in the format: mm-dd-yyyy")

    # Step 4: Check the day, month, and year ranges.
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

    # Step 5: Handle edge cases and errors.
    if date == "":
        raise ValueError("Date string cannot be empty")

    # Step 6: Return True if the date is valid, False otherwise.
    return True