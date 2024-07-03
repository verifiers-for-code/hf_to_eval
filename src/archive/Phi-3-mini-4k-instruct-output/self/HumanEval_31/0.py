import math

def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
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
    # Step 1: Identify the characteristics of a prime number
    if n <= 1:
        return False

    # Step 2: Check if 'n' is prime
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True