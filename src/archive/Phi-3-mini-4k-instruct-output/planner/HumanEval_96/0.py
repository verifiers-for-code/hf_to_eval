import math

def is_prime(num):
    """Check if a number is prime.
    
    Args:
    num (int): The number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def count_up_to(n):
    """Return an array of the first n prime numbers less than n.
    
    Args:
    n (int): The upper limit for prime numbers.
    
    Returns:
    list: A list of the first n prime numbers less than n.
    """
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
            if len(primes) == n:
                break
    return primes