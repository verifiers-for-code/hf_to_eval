def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Step 1: Start with the number just below n (n-1)
    divisor = n - 1

    # Step 2: Iterate through numbers in descending order
    while divisor > 1:
        # Step 2a: Check if the current number divides n evenly
        if n % divisor == 0:
            # Step 2b: Return the first number that divides n evenly
            return divisor
        # Step 3: Decrement the divisor and continue the loop
        divisor -= 1

    # If no divisor is found, return 1 (as 1 is the only divisor of 1)
    return 1