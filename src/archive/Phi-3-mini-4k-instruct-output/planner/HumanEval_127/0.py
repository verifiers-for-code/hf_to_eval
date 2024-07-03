import math

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    """
    Determine if the length of the intersection of two intervals is a prime number.

    Parameters:
    interval1 (tuple): A pair of integers representing the start and end of the first interval.
    interval2 (tuple): A pair of integers representing the start and end of the second interval.

    Returns:
    str: "YES" if the length of the intersection is a prime number, "NO" otherwise.
    """
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    if start > end:
        return "NO"

    length = end - start

    if is_prime(length):
        return "YES"
    else:
        return "NO"