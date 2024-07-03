def fib(n: int):
    """
    Return the n-th Fibonacci number.
    
    This function calculates the n-th Fibonacci number using a recursive approach.
    It handles edge cases for n=1 and n=2, and for n>2, it recursively calls fib(n-1) and fib(n-2)
    and adds the results. To optimize the solution, memoization is used to avoid redundant calculations.
    
    Parameters:
    n (int): The position of the Fibonacci number to be calculated.
    
    Returns:
    int: The n-th Fibonacci number.
    
    Example:
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # Memoization dictionary to store previously calculated Fibonacci numbers
    memo = {}

    def fib_recursive(n):
        # Base cases
        if n == 1:
            return 1
        elif n == 2:
            return 1

        # Check if the result is already in the memo dictionary
        if n in memo:
            return memo[n]

        # Recursive case: calculate the n-th Fibonacci number
        memo[n] = fib_recursive(n-1) + fib_recursive(n-2)
        return memo[n]

    return fib_recursive(n)