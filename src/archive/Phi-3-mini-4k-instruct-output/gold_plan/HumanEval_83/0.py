def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Step 1: Handle the special case
    if n == 1:
        return 1

    # Step 2: Calculate the count of n-digit numbers starting with 1
    start_with_one = 9 * (10 ** (n - 1))

    # Step 2: Calculate the count of n-digit numbers ending with 1
    # Note: Numbers ending with 1 have 9 options for the first digit (1-9)
    # and 10 options for the remaining (n-2) digits
    end_with_one = 9 * 10 ** (n - 2)

    # Step 3: Combine the calculations
    # Since numbers that start and end with 1 are counted twice,
    # we subtract the count of numbers that start and end with 1
    total_count = start_with_one + end_with_one - (9 * 10 ** (n - 2))

    return total_count