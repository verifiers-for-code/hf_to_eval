def is_simple_power(x, n):
    """
    Determines if a number x is a simple power of n.
    
    Args:
    x (int): The number to check.
    n (int): The base number.
    
    Returns:
    bool: True if x is a simple power of n, False otherwise.
    """
    # Edge case: x is 1
    if x == 1:
        return True
    
    # Edge case: n is 0
    if n == 0:
        return False
    
    # Initialize exponent variable
    exponent = 0
    
    # Loop until n**exponent equals x or exceeds a limit
    while n ** exponent <= x:
        if n ** exponent == x:
            return True
        exponent += 1
    
    # If loop ends without finding an integer exponent that makes n**exponent equal to x
    return False