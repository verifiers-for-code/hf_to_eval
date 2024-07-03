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
    1. Write a helper function to calculate the intersection of two intervals:
        a. If the end of the first interval is less than the start of the second or vice versa, they don't intersect
        b. Otherwise, find the maximum of the two starts, and the minimum of the two ends as the intersection's bounds
    
    2. In the main function, call the helper function to find the intersection
    
    3. Calculate the length of the intersection:
        a. Check if the start is less than or equal to the end
        b. If not, the intersection doesn't exist (length is 0 or negative)
        c. Otherwise, subtract the start from the end to get the length
    
    4. Determine if the length is a prime number:
        a. Implement a function to check for primality
        b. If the length is less than 2, it's not prime (return "NO")
        c. For other lengths, check divisibility from 2 to the square root of the length
    
    5. Return the appropriate result ("YES" or "NO") based on the length's primality
    
    6. Edge cases to consider:
        a. Same intervals (length 0)
        b. Intervals with no intersection
        c. Intervals with negative length"""

    def intersection_intervals(interval1, interval2):
        if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
            return None
        return (max(interval1[0], interval2[0]), min(interval1[1], interval2[1]))

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    inter = intersection_intervals(interval1, interval2)
    if inter is None:
        return "NO"

    length = inter[1] - inter[0]
    if length <= 0:
        return "NO"

    return "YES" if is_prime(length) else "NO"