def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21

    Action Plan:
    1. Check for base cases:
       - If n is 0, return 0
       - If n is 1, return 1
    2. For n > 1, implement the recursive formula:
       - The n-th Fibonacci number is the sum of the (n-1)th and (n-2)th Fibonacci numbers
    3. Use recursion:
       - Call the fib function twice within itself, with arguments (n-1) and (n-2)
    4. Combine the results:
       - Add the results of the two recursive calls
    5. Return the final sum
    
    Remember: The Fibonacci sequence starts with 0 and 1, and each subsequent number
    is the sum of the two preceding ones.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)