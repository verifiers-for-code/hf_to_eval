import math

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """Returns the value of x if n is a prime number, otherwise returns y."""
    if n <= 0:
        return y
    if is_prime(n):
        return x
    else:
        return y