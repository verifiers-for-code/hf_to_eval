import math

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Check if a number is the multiplication of three prime numbers."""
    if a < 2 or a > 99:
        return False

    for i in range(2, int(a**(1/3)) + 1):
        if is_prime(i):
            for j in range(i, int(a**(1/3)) + 1):
                if is_prime(j) and a % j == 0:
                    for k in range(j, int(a**(1/3)) + 1):
                        if is_prime(k) and i * j * k == a:
                            return True
    return False