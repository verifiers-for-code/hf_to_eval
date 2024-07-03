def closest_integer(value):
    """
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Args:
    value (str): A string representing a number.

    Returns:
    int: The closest integer to the input value, rounding away from zero if equidistant.

    Examples:
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15
    >>> closest_integer("14.5")
    15
    >>> closest_integer("-14.5")
    -15
    """
    # Convert the input value to a float
    num = float(value)

    # Round the number to the nearest integer
    rounded_num = round(num)

    # Check if the number is equidistant from two integers
    if abs(num - rounded_num) == 0.5:
        # If the number is positive, round up
        if num > 0:
            rounded_num += 1
        # If the number is negative, round down
        else:
            rounded_num -= 1

    return rounded_num