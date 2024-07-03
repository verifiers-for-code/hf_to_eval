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
    for i in range(2, int(a**(1/3)) + 1):
        if not is_prime(i):
            continue
        for j in range(i, int(a**(1/3)) + 1):
            if not is_prime(j):
                continue
            for k in range(j, int(a**(1/3)) + 1):
                if not is_prime(k):
                    continue
                if i * j * k == a:
                    return True
    return False