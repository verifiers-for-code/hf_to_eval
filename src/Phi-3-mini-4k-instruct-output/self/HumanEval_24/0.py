def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Action Plan:
    1. Define the function `largest_divisor` with a single integer input `n`.
    2. Implement the logic to find the largest divisor smaller than n:
        a. Calculate `largest_divisor_value` as floor division of n by (n - 1).
    3. Return `largest_divisor_value`.
    4. Make sure to consider and handle potential edge cases (e.g., n = 1, or n = 2).
    5. Remember that the function should not return 1 as the largest divisor since the problem statement asks for it to be smaller than n.
    """
    if n == 1:
        return None
    elif n == 2:
        return 1
    else:
        largest_divisor_value = n // (n - 1)
        return largest_divisor_value