def is_prime(n):
    """Helper function to check for primality"""
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Returns an array of the first n prime numbers less than n"""
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
            if len(primes) == n:
                break
    return primes