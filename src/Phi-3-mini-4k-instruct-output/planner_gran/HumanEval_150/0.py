import math

def is_prime(num):
    """Check if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """Return the value of x if n is a prime number, otherwise return the value of y.

    Args:
        n (int): The number to check for primality.
        x (int): The value to return if n is prime.
        y (int): The value to return if n is not prime.

    Returns:
        int: The value of x if n is prime, otherwise the value of y.

    Examples:
        >>> x_or_y(7, 34, 12)
        34
        >>> x_or_y(15, 8, 5)
        5
    """
    if isinstance(n, int) and n > 0 and isinstance(x, int) and isinstance(y, int):
        return x if is_prime(n) else y