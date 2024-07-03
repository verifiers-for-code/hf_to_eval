def is_prime(k: int) -> bool:
    """Check if a number k is prime.

    Args:
    k (int): The number to check.

    Returns:
    bool: True if k is prime, False otherwise.
    """
    if k < 2:
        return False
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0:
            return False
    return True

def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n.

    Args:
    n (int): The number to find the largest prime factor of.

    Returns:
    int: The largest prime factor of n.

    Examples:
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_prime = 2
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            largest_prime = i
    return largest_prime