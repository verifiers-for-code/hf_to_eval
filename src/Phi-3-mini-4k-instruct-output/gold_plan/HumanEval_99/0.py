def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.

    Action Plan:
    1. Check if the input string contains a decimal point.
       If it does, remove any trailing zeros after the decimal point.

    2. Convert the input string to a float.

    3. Check if the number ends with '.5':
       a. If it does, determine if it's positive or negative.
       b. For positive numbers ending in '.5', round up to the next integer.
       c. For negative numbers ending in '.5', round down to the next integer.

    4. If the number doesn't end with '.5':
       a. Use a standard rounding function to get the nearest integer.

    5. Handle the edge case of an empty string by returning 0.

    6. Return the resulting integer.

    Note: Import any necessary modules for mathematical operations like
    floor, ceil, and round.
    '''

    # Import necessary modules
    from math import floor, ceil

    # Check if the input string is empty
    if not value:
        return 0

    # Remove trailing zeros after decimal point
    value = value.rstrip('0')

    # Convert the input string to a float
    num = float(value)

    # Check if the number ends with '.5'
    if num % 1 == 0.5:
        # Determine if it's positive or negative
        if num > 0:
            # Round up to the next integer
            return ceil(num)
        else:
            # Round down to the next integer
            return floor(num)
    else:
        # Use a standard rounding function to get the nearest integer
        return round(num)