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
    If the two intervals don't intersect, return "NO".


    [input/output] samples:
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    

    Action Plan:
    1. Calculate the start of the intersection by finding the maximum of the start points of the two intervals.
    2. Calculate the end of the intersection by finding the minimum of the end points of the two intervals.
    3. Calculate the length of the intersection by subtracting the start from the end. If the length is not positive, the intervals do not intersect, so return "NO".
    4. Implement a helper function to check if a number is prime:
       a. Check if the number is less than 2, in which case it's not prime.
       b. Check if the number is 2, in which case it is prime.
       c. Iterate from 2 to the number, checking if the number is divisible by any of these values. If it is, it's not prime.
       d. If the number is not divisible by any of these values, it's prime.
    5. Use the helper function to check if the length of the intersection is prime. If it is, return "YES", otherwise return "NO"."""

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    if start >= end:
        return "NO"

    length = end - start
    return "YES" if is_prime(length) else "NO"