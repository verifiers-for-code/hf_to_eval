def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Start with the number just below n (n-1)
    divisor = n - 1
    
    # Iterate through numbers in descending order
    while divisor > 0:
        # For each number, check if it divides n evenly
        if n % divisor == 0:
            # Use the modulo operator (%) to check for even division
            return divisor
        # Decrement the divisor
        divisor -= 1
    
    # If no divisor is found, return 1 (since 1 divides all numbers evenly)
    return 1