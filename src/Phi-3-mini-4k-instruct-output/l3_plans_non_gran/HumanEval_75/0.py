def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Return True if the given number is the multiplication of 3 prime numbers, False otherwise."""
    prime_factors = []
    for i in range(2, a + 1):
        if a % i == 0 and is_prime(i):
            prime_factors.append(i)
            a //= i
            if len(prime_factors) == 3:
                return True
    return False