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
    """Return True if the given number is the multiplication of 3 prime numbers, False otherwise."""
    if a < 3:
        return False
    for i in range(2, a):
        if is_prime(i):
            count = 0
            for j in range(2, int(math.sqrt(a)) + 1):
                if a % j == 0:
                    if is_prime(j):
                        count += 1
                        if count == 2:
                            return True
                        break
    return False