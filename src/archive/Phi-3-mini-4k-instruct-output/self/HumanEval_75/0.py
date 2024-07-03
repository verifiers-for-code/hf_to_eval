def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    """Find all prime factors of a number."""
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            if is_prime(divisor):
                factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def is_multiply_prime(a):
    """Return True if the given number is the multiplication of 3 prime numbers, False otherwise."""
    # Input validation
    if not isinstance(a, int) or a < 1 or a > 100:
        return False

    # Factorization logic
    factors = prime_factors(a)

    # Handle prime factors
    if len(factors) == 3 and all(is_prime(factor) for factor in factors):
        return True
    else:
        return False