import math

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_length(string):
    """Return True if the length of the string is a prime number, False otherwise."""
    if not isinstance(string, str):
        return False
    if not string:
        return False
    length = len(string)
    return is_prime(length)