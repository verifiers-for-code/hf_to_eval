def closest_integer(value):
    """
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Args:
    value (str): A string representing a number.

    Returns:
    int: The closest integer to the input value.
    """
    import math

    # Step 1: Check if the input string contains a decimal point.
    if '.' in value:
        # Remove any trailing zeros after the decimal point.
        value = value.rstrip('0').rstrip('.')

    # Step 2: Convert the input string to a float.
    num = float(value)

    # Step 3: Check if the number ends with '.5'
    if num % 1 == 0.5:
        # Determine if it's positive or negative
        if num > 0:
            # For positive numbers ending in '.5', round up to the next integer.
            return math.ceil(num)
        else:
            # For negative numbers ending in '.5', round down to the next integer.
            return math.floor(num)

    # Step 4: If the number doesn't end with '.5', use a standard rounding function to get the nearest integer.
    return round(num)