import datetime

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 for months 1,3,5,7,8,10,12.
       And the number of days is not less than 1 or higher than 30 for months 4,6,9,11.
       And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy
    
    Args:
        date (str): The date string to validate.
        
    Returns:
        bool: True if the date is valid, False otherwise.
    """
    # Step 1: Check if the input date string is empty
    if not date:
        return False
    
    # Step 2: Split the date string into month, day, and year components
    month, day, year = date.split('-')
    
    # Step 3: Validate the date format
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        return False
    
    # Step 4: Validate the month and day values
    month = int(month)
    day = int(day)
    
    if month < 1 or month > 12:
        return False
    
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        if day < 1 or day > 29:
            # Check for leap year
            if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
                return False
            else:
                return True
        else:
            return False
    else:
        return False
    
    return True