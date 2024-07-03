def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    
    Action Plan:
    1. Define a function named sum_to_n that takes an integer n as input.
    2. Initialize a variable to store the sum, set to 0.
    3. Use a loop to iterate from 1 to n (inclusive).
    4. In each iteration, add the current number to the sum.
    5. After the loop, return the final sum.
    6. Consider using a more efficient approach, such as the formula for the sum of an arithmetic series, to optimize the function.
    
    Note: The formula for the sum of an arithmetic series is n * (n + 1) / 2, which can be used to implement the function more efficiently."""
    
    # Initialize sum to 0
    sum = 0
    
    # Iterate from 1 to n (inclusive)
    for i in range(1, n+1):
        sum += i
    
    # Return the final sum
    return sum