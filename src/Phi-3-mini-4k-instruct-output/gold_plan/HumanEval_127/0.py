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

    Action Plan:
    1. Define a helper function `is_prime(num)` to check if a number is prime:
       - Handle edge cases (0, 1, and 2)
       - Use a loop to check for divisibility up to the number itself
       - Return True if prime, False otherwise

    2. Find the intersection of the two intervals:
       - Calculate the start of the intersection (maximum of the two start points)
       - Calculate the end of the intersection (minimum of the two end points)

    3. Calculate the length of the intersection:
       - Subtract the start from the end
       - If the length is 0 or negative, there's no intersection

    4. Check if the length is prime:
       - Use the is_prime() function on the length

    5. Return the result:
       - If the length is positive and prime, return "YES"
       - Otherwise, return "NO"

    [input/output] samples:
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    """

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    start_intersection = max(interval1[0], interval2[0])
    end_intersection = min(interval1[1], interval2[1])

    if start_intersection > end_intersection:
        return "NO"

    length_intersection = end_intersection - start_intersection

    if length_intersection > 0 and is_prime(length_intersection):
        return "YES"
    else:
        return "NO"