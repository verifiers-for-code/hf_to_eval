def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    count = 0
    max_num = 10**n - 1

    # Step 1: Generate n-digit positive integers starting from 1 up to the maximum n-digit number
    for num in range(1, max_num + 1):
        # Step 2: Check if the number starts or ends with 1
        if str(num)[0] == '1' or str(num)[-1] == '1':
            count += 1

    return count