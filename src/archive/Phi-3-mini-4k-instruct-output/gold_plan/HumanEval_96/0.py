def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_up_to(n):
    """Return an array of the first n prime numbers less than n."""
    primes = []
    for num in range(2, n):
        if is_prime(num):
            primes.append(num)
            if len(primes) == n:
                break
    return primes