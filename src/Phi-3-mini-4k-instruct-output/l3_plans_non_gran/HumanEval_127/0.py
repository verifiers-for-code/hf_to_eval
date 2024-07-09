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
    1. Parse the input intervals (interval1 and interval2) and extract their start and end points.
    2. Calculate the intersection of the two intervals:
        - Find the maximum start point (max_start) and minimum end point (min_end) of the two intervals.
        - Calculate the length of the intersection as max_start - min_end + 1.
    3. Check if the intervals do not intersect:
        - If the calculated length is less than 1, return "NO".
    4. Calculate the square root of the length.
    5. Check if the length is a prime number:
        - Iterate from 2 to the square root of the length.
        - Check if the length is divisible by any number in this range.
        - If the length is divisible, return "NO".
    6. If the length is not divisible by any number, return "YES"."""

    # Step 1: Parse the input intervals
    start1, end1 = interval1
    start2, end2 = interval2

    # Step 2: Calculate the intersection
    max_start = max(start1, start2)
    min_end = min(end1, end2)
    intersection_length = max(0, max_start - min_end + 1)

    # Step 3: Check if the intervals do not intersect
    if intersection_length < 1:
        return "NO"

    # Step 4: Calculate the square root of the length
    sqrt_length = math.sqrt(intersection_length)

    # Step 5: Check if the length is a prime number
    for i in range(2, int(sqrt_length) + 1):
        if intersection_length % i == 0:
            return "NO"

    # Step 6: If the length is not divisible by any number, return "YES"
    return "YES"