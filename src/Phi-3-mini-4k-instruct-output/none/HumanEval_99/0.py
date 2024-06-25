def closest_integer(value):
    """
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Args:
    value (str): A string representing a number

    Returns:
    int: The closest integer to the input value

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
    value_float = float(value)

    # Round the float value to the nearest integer
    rounded_value = round(value_float)

    # Check if the rounded value is equidistant from two integers
    if abs(value_float - rounded_value) == 0.5:
        # If the rounded value is positive, round it away from zero
        if rounded_value > 0:
            return rounded_value + 1
        # If the rounded value is negative, round it away from zero
        else:
            return rounded_value - 1
    else:
        # Return the rounded value if it's not equidistant from two integers
        return rounded_value