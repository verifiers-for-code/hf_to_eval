def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    
    Action Plan:
    1. Implement a loop to generate n-digit positive integers starting from 1 up to the maximum n-digit number (10^n - 1)
    
    2. For each generated number:
        a. Check if the number starts or ends with 1 by taking appropriate digits from the number
        b. If it meets the criteria, increment the count counter
    
    3. Return the count of numbers that start or end with 1
    
    4. Note that the loop should efficiently cover the n-digit number range without iterating through all possible integers
    """
    count = 0
    for i in range(1, 10**n):
        if str(i)[0] == '1' or str(i)[-1] == '1':
            count += 1
    return count