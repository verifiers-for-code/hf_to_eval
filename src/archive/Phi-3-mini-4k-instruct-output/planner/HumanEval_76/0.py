def is_simple_power(x, n):
    """
    This function checks if a number x is a simple power of n.
    
    Args:
    x (int): The number to check.
    n (int): The base number.
    
    Returns:
    bool: True if x is a simple power of n, False otherwise.
    
    The function returns True if n raised to the power of an integer is equal to x.
    It returns False in all other cases.
    """
    # Step 2: Calculate n raised to the power of int
    result = n ** int(n)
    
    # Step 3 & 4: Compare the result with x
    if result == x:
        return True
    else:
        return False