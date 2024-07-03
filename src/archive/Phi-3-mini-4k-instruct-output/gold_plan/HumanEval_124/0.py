def valid_date(date):
    """Validates a given date string and returns True if the date is valid, otherwise False."""
    try:
        # Remove leading or trailing whitespace
        date = date.strip()
        
        # Split the date string into month, day, and year components
        month, day, year = date.split('-')
        
        # Convert components to integers
        month, day, year = int(month), int(day), int(year)
        
        # Check if the month is valid (between 1 and 12)
        if not 1 <= month <= 12:
            return False
        
        # Lists of months with 31 days and 30 days
        months_31_days = [1, 3, 5, 7, 8, 10, 12]
        months_30_days = [4, 6, 9, 11]
        
        # Check day validity based on the month
        if month in months_31_days:
            if not 1 <= day <= 31:
                return False
        elif month in months_30_days:
            if not 1 <= day <= 30:
                return False
        elif month == 2:
            if not 1 <= day <= 29:
                return False
            # Check for leap year
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                if day > 29:
                    return False
        else:
            return False
        
        return True
    
    except Exception:
        return False