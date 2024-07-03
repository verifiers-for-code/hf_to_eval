import math

def is_prime(n):
    """Check if a number is prime.
    
    Args:
    n (int): The number to check.
    
    Returns:
    bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """Return x if n is prime, otherwise return y.
    
    Args:
    n (int): The number to check for primality.
    x (int): The value to return if n is prime.
    y (int): The value to return if n is not prime.
    
    Returns:
    int: x if n is prime, otherwise y.
    """
    if n <= 1:
        return y
    if is_prime(n):
        return x
    return y