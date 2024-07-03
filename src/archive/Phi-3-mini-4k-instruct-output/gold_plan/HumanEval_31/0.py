def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    
    Action Plan:
    1. Check if n is less than 2. If so, return False as numbers less than 2 are not prime.
    2. Loop through numbers from 2 to n-1 (exclusive):
       a. Check if n is divisible by the current number (use modulo operator %).
       b. If n is divisible by any number in this range, return False immediately.
    3. If the loop completes without finding any divisors, return True.
    
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
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True