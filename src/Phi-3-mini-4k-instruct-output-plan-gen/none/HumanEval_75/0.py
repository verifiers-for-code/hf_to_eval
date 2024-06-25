
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Return True if the given number is the multiplication of 3 prime numbers, False otherwise."""
    if a < 3:
        return False
    primes = []
    for i in range(2, a):
        if is_prime(i):
            primes.append(i)
            if len(primes) == 3:
                break
    return a == primes[0] * primes[1] * primes[2]