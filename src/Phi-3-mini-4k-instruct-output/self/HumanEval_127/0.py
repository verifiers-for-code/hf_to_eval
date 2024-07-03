import math

def intersection(interval1, interval2):
    """
    You are given two intervals, where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end) includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two intervals is a prime number.
    If the length of the intersection is a prime number, return "YES", otherwise, return "NO".
    If the two intervals don't intersect, return "NO".
    """

    def calculate_intersection(interval1, interval2):
        """
        Helper function to calculate the intersection of two intervals.
        """
        if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
            return None  # No intersection
        return (max(interval1[0], interval2[0]), min(interval1[1], interval2[1]))

    def is_prime(n):
        """
        Helper function to check if a number is prime.
        """
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    intersection_interval = calculate_intersection(interval1, interval2)
    if intersection_interval is None:
        return "NO"

    length = intersection_interval[1] - intersection_interval[0]
    if length <= 0:
        return "NO"

    return "YES" if is_prime(length) else "NO"