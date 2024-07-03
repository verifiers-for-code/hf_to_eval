def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
    1. Understand the problem:
       - The function takes a positive integer n as input
       - It needs to count the number of n-digit positive integers that either start or end with 1
    
    2. Calculate the total count of n-digit positive integers:
       - Use the formula 10^n to calculate the total count of n-digit positive integers
       - This includes numbers with any digit in the first position
    
    3. Calculate the count of n-digit positive integers that start with 1:
       - Use the formula 9 * 10^(n-1) to calculate the count of n-digit positive integers that start with 1
       - This includes numbers with 1 in the first position and any digit in the remaining positions
    
    4. Calculate the count of n-digit positive integers that end with 1:
       - Use the formula 9 * 10^(n-1) to calculate the count of n-digit positive integers that end with 1
       - This includes numbers with 1 in the last position and any digit in the remaining positions
    
    5. Subtract the overlapping count to avoid double counting:
       - Calculate the overlap by finding the count of numbers that both start and end with 1
       - Subtract this overlap from the total count to avoid double counting
    
    6. Return the final count:
       - Return the calculated count of n-digit positive integers that either start or end with 1
    
    Additional implementation details:
    - Use the appropriate mathematical operations and formulae to calculate the counts
    - Ensure that the function handles input values of n correctly
    - Consider adding input validation to ensure n is a positive integer
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    total_count = 10**n
    start_count = 9 * 10**(n-1)
    end_count = 9 * 10**(n-1)
    overlap_count = 9 * 10**(n-2)
    
    return total_count - overlap_count + start_count + end_count