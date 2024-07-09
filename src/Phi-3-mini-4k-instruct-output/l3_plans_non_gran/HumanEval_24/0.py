def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Action Plan:
    1. Understand the problem: Find the largest number that divides n evenly, smaller than n.
    2. Initialize a variable to store the largest divisor, set it to 0.
    3. Iterate through numbers from 1 to n-1 (inclusive):
        a. Check if the current number is a divisor of n (i.e., n % i == 0).
        b. If it is, and the current number is larger than the largest divisor, update the largest divisor.
    4. After iterating through the range, return the largest divisor.
    5. Consider handling edge cases, such as n being 0 or a negative number.
    """
    if n <= 0:
        return None
    
    largest_divisor = 0
    for i in range(1, n):
        if n % i == 0 and i > largest_divisor:
            largest_divisor = i
    
    return largest_divisor