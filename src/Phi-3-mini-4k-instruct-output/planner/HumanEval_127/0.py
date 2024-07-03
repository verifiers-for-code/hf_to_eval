import math

def intersection(interval1, interval2):
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".


    [input/output] samples:
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    

    Action Plan:
    1. Define the function `intersection` with two parameters: `interval1` and `interval2`, each a tuple of two integers representing the start and end of the interval.
    2. Find the intersection of the two intervals by taking the maximum of the start values and the minimum of the end values.
    3. Calculate the length of the intersection by subtracting the start value from the end value.
    4. Check if the length of the intersection is a prime number:
        a. Initialize a flag `is_prime` to `True`.
        b. Iterate from 2 to the square root of the length of the intersection.
        c. For each number in the iteration, check if it divides the length of the intersection evenly.
        d. If a divisor is found, set `is_prime` to `False` and break the loop.
    5. Return "YES" if `is_prime` is `True`, and "NO" otherwise.
    6. Consider edge cases, such as intervals that don't intersect or have a length of 0."""

    # Find the intersection of the two intervals
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    # Calculate the length of the intersection
    length = end - start

    # Check if the length of the intersection is a prime number
    if length <= 1:
        return "NO"
    is_prime = True
    for i in range(2, int(math.sqrt(length)) + 1):
        if length % i == 0:
            is_prime = False
            break

    return "YES" if is_prime else "NO"