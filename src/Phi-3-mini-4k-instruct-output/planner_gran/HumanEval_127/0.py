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
    

    1. Calculate the intersection of the two intervals:
       - Find the maximum of the start values (minimum of the two start values)
       - Find the minimum of the end values (maximum of the two end values)
       - Store the intersection interval in a variable (e.g., intersection_start, intersection_end)
    
    2. Calculate the length of the intersection:
       - Subtract the intersection start from the intersection end to get the length
       - Store the length in a variable (e.g., intersection_length)
    
    3. Check if the length is a prime number:
       - Define a helper function (is_prime) to check if a number is prime
       - Call the is_prime function with the intersection length as an argument
       - If the length is prime, return "YES"
    
    4. Handle the case where the intervals don't intersect:
       - Check if the intersection start is greater than the intersection end
       - If true, return "NO" (indicating no intersection)
    
    Additional implementation details:
    - Use appropriate variable names and data types
    - Consider handling edge cases, such as empty intervals or identical intervals
    - Ensure the is_prime function correctly checks for primality
    - Use a consistent coding style and follow best practices for Python programming"""

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    intersection_start = max(interval1[0], interval2[0])
    intersection_end = min(interval1[1], interval2[1])

    if intersection_start > intersection_end:
        return "NO"

    intersection_length = intersection_end - intersection_start

    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"