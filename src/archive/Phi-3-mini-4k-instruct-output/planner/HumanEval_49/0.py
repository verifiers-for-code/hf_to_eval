def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).
    
    This function calculates 2^n modulo p, taking into account potential overflow issues.
    It uses the ** operator to calculate 2^n and the modulo operator (%) to ensure the result is within the range of p.
    
    Parameters:
    n (int): The exponent for the power of 2.
    p (int): The modulo value.
    
    Returns:
    int: The result of (2^n) % p.
    
    Examples:
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    # Calculate 2^n using the ** operator
    result = 2 ** n
    
    # Handle potential overflow issues by using the modulo operator (%)
    # to ensure the result is within the range of p
    return result % p