def is_prime(num):
    """Check if a number is prime."""
    if num in (0, 1):
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    """Determine if the length of the intersection of two intervals is a prime number."""
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    if start > end:
        return "NO"

    length = end - start
    if is_prime(length):
        return "YES"
    else:
        return "NO"