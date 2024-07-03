def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Base case: if n is 1, there are only two possibilities (1 or 2)
    if n == 1:
        return 2
    
    # For n > 1, derive a formula to calculate the count of n-digit numbers that start or end with 1
    # Consider the possibilities for the first digit (1 or not 1)
    # Consider the possibilities for the last digit (1 or not 1)
    # Calculate the count of numbers that meet the conditions
    count = 0
    for i in range(10):
        for j in range(10):
            if i == 1 or j == 1:
                count += 1
    
    return count