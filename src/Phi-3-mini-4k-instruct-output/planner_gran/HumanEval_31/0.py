def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    
    Parameters:
    n (int): The number to check for primality.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    
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
    
    # Handle edge cases
    if n < 2:
        return False
    
    # Check for divisibility by 2 and 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Implement a loop to check for other divisors
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    # Return the result
    return True