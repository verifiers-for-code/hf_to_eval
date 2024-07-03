def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    

    Action Plan:
    1. Define a recursive helper function to calculate the factorial of a single number:
        - This function will have a base case for 0! (which is 1)
        - Calculate n! recursively as n * factorial(n-1)
    
    2. Implement the special factorial function using a nested loop:
        - Start with n! and for each decremental value (n-1!, n-2!, ...), multiply it with the previously computed factorial
    
    3. Optimize the implementation:
        - Instead of a nested loop, use an iterative approach to compute each factorial and multiply them iteratively
        - This approach will help reduce the computational complexity
    
    4. Test the function:
        - Confirm the special factorial returns the expected results for the given test cases
        - Verify the function's performance with increasingly larger input values
    
    5. Validate edge cases:
        - Test the function with input values of 1, as factorial of 1 should equal 1 regardless of the iterations
        - Ensure negative input values result in an error or an appropriate message, as factorial is undefined for negative numbers"""

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(n, 0, -1):
            result *= factorial(i)
        return result