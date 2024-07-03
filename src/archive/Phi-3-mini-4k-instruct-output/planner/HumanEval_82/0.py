import math

def is_prime(n):
    """Check if a number is prime.
    
    Args:
    n (int): The number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_length(string):
    """Check if the length of a string is a prime number.
    
    Args:
    string (str): The input string.
    
    Returns:
    bool: True if the length of the string is prime, False otherwise.
    """
    length = len(string)
    return is_prime(length)