def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.
    
    Action Plan:
    1. Define the function sum_to_n with a single parameter n:
       - n is a non-negative integer
    
    2. Initialize a variable to store the sum of numbers from 1 to n:
       - This variable will be used to accumulate the sum of numbers
    
    3. Calculate the sum of numbers from 1 to n:
       - Use a loop to iterate from 1 to n (inclusive)
       - In each iteration, add the current number to the sum variable
    
    4. Return the calculated sum:
       - The function should return the final sum of numbers from 1 to n
    
    Additional implementation details:
    - Use a for loop or a recursive approach to calculate the sum
    - Ensure the function handles edge cases, such as n = 0 or n = 1, correctly
    - Consider using a more efficient formula, such as n * (n + 1) / 2, to calculate the sum
    - Use appropriate variable names and comments to make the code readable and understandable
    """
    # Initialize the sum variable
    total_sum = 0
    
    # Calculate the sum of numbers from 1 to n
    for i in range(1, n+1):
        total_sum += i
    
    # Return the calculated sum
    return total_sum