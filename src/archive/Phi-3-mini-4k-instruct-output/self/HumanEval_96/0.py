import math

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Returns an array of the first n prime numbers less than n."""
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
            if len(primes) == n:
                break
    return primes