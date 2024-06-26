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
    # Note: The first digit can't be 0, so there are 9 options (1-9)
    end_with_one = 9 * (10 ** (n - 2))

    # Step 3: Combine the calculations
    # The total count will be the sum of start_with_one and end_with_one,
    # minus the double-counted numbers (those that start and end with 1)
    total_count = start_with_one + end_with_one - (start_with_one * end_with_one)

    return total_count