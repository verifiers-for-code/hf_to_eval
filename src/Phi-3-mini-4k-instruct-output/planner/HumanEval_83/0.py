def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    
    Action Plan:
    1. Understand the problem:
        - The function takes a positive integer n as input
        - It returns the count of n-digit positive integers that start or end with 1
    
    2. Calculate the total number of n-digit positive integers:
        - Use the formula 10^(n-1) to get the total count
    
    3. Calculate the number of n-digit positive integers that start with 1:
        - Use the formula 9 * 10^(n-2) to get the count
    
    4. Calculate the number of n-digit positive integers that end with 1:
        - Use the formula 9 * 10^(n-2) to get the count
    
    5. Combine the results:
        - Add the counts from steps 3 and 4 to get the final count
    
    Note: Use the correct mathematical operations and formulas to calculate the counts.
    Be careful with the exponentiation and multiplication operations.
    """
    total_count = 10 ** (n - 1)
    start_count = 9 * 10 ** (n - 2)
    end_count = 9 * 10 ** (n - 2)
    result = start_count + end_count
    return result