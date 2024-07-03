def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Step 1: Start with the number just below n (n-1)
    divisor = n - 1

    # Step 2: Iterate through numbers in descending order
    while divisor > 1:
        # Step 2a: For each number, check if it divides n evenly
        if n % divisor == 0:
            # Step 2b: Use the modulo operator (%) to check for even division
            return divisor
        # Step 4: Continue the loop until a divisor is found
        divisor -= 1

    # If no divisor is found, return 1 (as 1 is a divisor of all numbers)
    return 1