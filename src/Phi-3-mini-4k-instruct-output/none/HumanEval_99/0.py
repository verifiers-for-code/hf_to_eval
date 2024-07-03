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
    '''
    # Convert the string to a float
    num = float(value)

    # Check if the number is an integer
    if num.is_integer():
        return int(num)

    # Calculate the distance to the nearest integer
    distance_to_lower = num - int(num)
    distance_to_upper = int(num) - num

    # Check if the number is equidistant from two integers
    if distance_to_lower == distance_to_upper:
        # Round away from zero
        if num > 0:
            return int(num) + 1
        else:
            return int(num) - 1

    # Return the closest integer
    if distance_to_lower < distance_to_upper:
        return int(num)
    else:
        return int(num) + 1