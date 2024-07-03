def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Step 2: Implement the logic to find the largest divisor smaller than n
    if n == 1:
        return None  # Edge case: n = 1
    elif n == 2:
        return 1  # Edge case: n = 2
    else:
        largest_divisor_value = n // (n - 1)
    
    return largest_divisor_value