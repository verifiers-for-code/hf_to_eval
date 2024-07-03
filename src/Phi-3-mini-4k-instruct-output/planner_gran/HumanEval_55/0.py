def fib(n: int):
    """
    Return n-th Fibonacci number.
    
    Parameters:
    n (int): The position of the Fibonacci number to be returned.
    
    Returns:
    int: The n-th Fibonacci number.
    
    Examples:
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    
    Action Plan:
    1. Define the function `fib` with a single parameter `n` of type `int`:
       - The function should return the n-th Fibonacci number
    
    2. Handle edge cases:
       - If `n` is 1, return 1 (base case)
       - If `n` is 2, return 1 (base case)
    
    3. Implement the recursive formula for `n` greater than 2:
       - Use the formula `fib(n) = fib(n-1) + fib(n-2)`
       - Call the `fib` function recursively with `n-1` and `n-2` as arguments
       - Add the results of these recursive calls to get the n-th Fibonacci number
    
    4. Return the calculated Fibonacci number:
       - The function should return an `int` value representing the n-th Fibonacci number
    
    Additional implementation details:
    - Ensure the function handles invalid input values (e.g., non-integer or negative `n`) correctly
    - Consider adding a docstring to the function to explain its purpose, parameters, and return value
    - Use meaningful variable names and follow PEP 8 conventions for code readability
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")
    
    if n == 1 or n == 2:
        return 1
    
    return fib(n-1) + fib(n-2)