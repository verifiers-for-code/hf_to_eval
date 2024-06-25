
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert the integer to a string
    x_str = str(x)

    # Calculate the effective shift
    effective_shift = shift % len(x_str)

    # Perform circular shift
    shifted_str = x_str[-effective_shift:] + x_str[:-effective_shift]

    return shifted_str