def is_simple_power(x, n):
    """
    Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    # Handle edge cases
    if x == 1:
        return True
    if n == 0:
        return False
    
    # Initialize an exponent variable to 0
    exponent = 0
    
    # Begin a while loop, continuing until n**exponent either equals x or reaches a limit
    while n ** exponent < x:
        exponent += 1
        # Check for potential integer overflow or limits for n
        if exponent > 100:
            return False
    
    # If the loop ends without finding an integer exponent that makes n**exponent equal to x, return False
    if n ** exponent == x:
        return True
    else:
        return False