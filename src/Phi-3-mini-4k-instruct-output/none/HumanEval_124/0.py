from datetime import datetime

def valid_date(date):
    """Validates a given date string and returns True if the date is valid, otherwise False."""
    # Check if the date string is empty
    if not date:
        return False

    # Split the date string into month, day, and year
    try:
        month, day, year = map(int, date.split('-'))
    except ValueError:
        return False

    # Check if the month and day are within valid ranges
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return day > 31
        elif month in [4, 6, 9, 11]:
            return day > 30
        elif month == 2:
            # Check for leap year
            is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            return day <= 29 if not is_leap_year else day <= 28
        else:
            return False

    # Check if the date is in the correct format
    try:
        datetime.strptime(date, '%m-%d-%Y')
    except ValueError:
        return False

    return True