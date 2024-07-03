import math

def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    Parameters:
    n (int): The number to check for primality.
    
    Returns:
    bool: True if n is prime, False otherwise.
    
    Examples:
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    # Step 1: Handle edge cases
    if n <= 1:
        return False
    
    # Step 2: Implement the primality test
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    # Step 3: Return the result
    return True