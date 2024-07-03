def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    

    Action Plan:
    1. Define the function `fib(n)` with an integer parameter `n`.
    2. Handle edge cases:
        - If `n` is 1, return 1 (the first Fibonacci number).
        - If `n` is 2, return 1 (the second Fibonacci number).
    3. Implement the recursive formula:
        - For `n > 2`, recursively call `fib(n-1)` and `fib(n-2)` and add the results.
    4. Optimize the solution:
        - Consider using memoization or dynamic programming to avoid redundant calculations.
    5. Return the result:
        - Return the calculated Fibonacci number for the given `n`.
    
    Note: Be mindful of the recursive formula and its implications. Consider optimizing the solution to improve performance."""
    
    # Handle edge cases
    if n == 1:
        return 1
    elif n == 2:
        return 1
    
    # Implement the recursive formula
    def fib_helper(n):
        if n == 1 or n == 2:
            return 1
        else:
            return fib_helper(n-1) + fib_helper(n-2)
    
    # Optimize the solution using memoization
    memo = {}
    def fib_memo(n):
        if n in memo:
            return memo[n]
        if n == 1 or n == 2:
            memo[n] = 1
        else:
            memo[n] = fib_memo(n-1) + fib_memo(n-2)
        return memo[n]
    
    # Return the result using the optimized solution
    return fib_memo(n)