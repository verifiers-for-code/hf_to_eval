import math

def special_factorial(n):
    """
    The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    
    1. Initialize a variable to store the result (factorial) and set it to 1
       - This variable will hold the final result of the special factorial calculation
    
    2. Create a loop that iterates from n down to 1 (inclusive)
       - Use a for loop with a range that starts from n and ends at 1, with a step of -1
    
    3. Inside the loop, calculate the factorial of the current number (i)
       - Use the factorial formula: i! = i * (i-1) *... * 1
       - You can use a recursive approach or an iterative approach to calculate the factorial
    
    4. Multiply the current factorial with the result variable
       - This will update the result variable with the new factorial value
    
    5. After the loop, return the final result
       - This is the special factorial of the input integer n
    
    Additional implementation details:
    - Use a suitable data type to store the result (e.g., int or float)
    - Consider using a more efficient algorithm for calculating factorials, such as memoization or using the math.factorial function
    - Ensure that the function handles invalid input values (e.g., non-integer or negative values) correctly
    - Consider adding error handling for edge cases, such as n being 0 or 1
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    result = 1
    for i in range(n, 0, -1):
        result *= math.factorial(i)
    
    return result