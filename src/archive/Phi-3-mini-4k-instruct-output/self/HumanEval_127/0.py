def intersection(interval1, interval2):
    """Determine if the length of the intersection of two intervals is a prime number."""
    
    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def intersect(interval1, interval2):
        """Calculate the intersection of two intervals."""
        start1, end1 = interval1
        start2, end2 = interval2
        if end1 < start2 or end2 < start1:
            return None
        return (max(start1, start2), min(end1, end2))

    intersection_interval = intersect(interval1, interval2)
    
    if intersection_interval is None:
        return "NO"
    
    length = intersection_interval[1] - intersection_interval[0]
    
    if length <= 1:
        return "NO"
    
    return "YES" if is_prime(length) else "NO"