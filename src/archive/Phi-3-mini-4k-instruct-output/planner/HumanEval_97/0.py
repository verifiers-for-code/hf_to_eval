def multiply(a, b):
    """
    This function takes two integers as input and returns the product of their unit digits.
    
    Args:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The product of the unit digits of the input integers.
    
    Examples:
    >>> multiply(148, 412)
    16
    >>> multiply(19, 28)
    72
    >>> multiply(2020, 1851)
    0
    >>> multiply(14, -15)
    20
    """
    # Extract the unit digits of a and b
    unit_digit_a = a % 10
    unit_digit_b = b % 10
    
    # Multiply the unit digits
    result = unit_digit_a * unit_digit_b
    
    return result