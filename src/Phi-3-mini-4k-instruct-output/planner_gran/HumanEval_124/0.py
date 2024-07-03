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
    

    1. Input validation:
       - Check if the input date string is empty
       - If empty, return False (invalid date)
    
    2. Split the date string into month, day, and year components:
       - Use the appropriate string method to split the date string into three parts
       - Assign each part to separate variables (month, day, year)
    
    3. Validate the month:
       - Check if the month is less than 1 or greater than 12
       - If invalid, return False (invalid date)
    
    4. Validate the day:
       - Check if the month is 1, 3, 5, 7, 8, 10, or 12
       - If true, check if the day is less than 1 or greater than 31
       - If true, return False (invalid date)
       - If false, check if the month is 4, 6, 9, or 11
       - If true, check if the day is less than 1 or greater than 30
       - If true, return False (invalid date)
       - If false, check if the month is 2
       - If true, check if the day is less than 1 or greater than 29
       - If true, return False (invalid date)
       - If false, return True (valid day)
    
    5. Validate the year:
       - Check if the year is less than 0
       - If true, return False (invalid date)
    
    6. Validate the date format:
       - Check if the month and day are separated by a dash (-)
       - Check if the day and year are separated by a dash (-)
       - Check if the year is separated by a dash (-)
       - If any of these conditions are not met, return False (invalid date)
    
    7. If all validations pass, return True (valid date)"""
    
    # Input validation
    if not date:
        return False
    
    # Split the date string into month, day, and year components
    month, day, year = date.split('-')
    
    # Validate the month
    if not (1 <= int(month) <= 12):
        return False
    
    # Validate the day
    if (int(month) in [1, 3, 5, 7, 8, 10, 12] and not (1 <= int(day) <= 31)) or \
       (int(month) in [4, 6, 9, 11] and not (1 <= int(day) <= 30)) or \
       (int(month) == 2 and not (1 <= int(day) <= 29)):
        return False
    
    # Validate the year
    if int(year) < 0:
        return False
    
    # Validate the date format
    if not (month.isdigit() and day.isdigit() and year.isdigit() and '-' in date):
        return False
    
    # If all validations pass, return True
    return True