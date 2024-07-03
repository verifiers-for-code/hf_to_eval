from datetime import datetime

def valid_date(date):
    """Validates a given date string and returns True if the date is valid, otherwise False."""
    try:
        # Check if the date string is in the correct format
        datetime.strptime(date, '%m-%d-%Y')
        
        # Split the date string into month, day, and year
        month, day, year = date.split('-')
        
        # Convert month, day, and year to integers
        month, day, year = int(month), int(day), int(year)
        
        # Check if the month is between 1 and 12
        if month < 1 or month > 12:
            return False
        
        # Check if the day is valid for the given month
        if month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31):
            return False
        elif month in [4, 6, 9, 11] and (day < 1 or day > 30):
            return False
        elif month == 2 and (day < 1 or day > 29):
            return False
        elif month == 2 and day == 29 and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            return False
        
        return True
    
    except ValueError:
        # If the date string is not in the correct format or the day is invalid, return False
        return False