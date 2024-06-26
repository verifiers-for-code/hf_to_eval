def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # Step 1: Check for base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Step 2: Implement the recursive formula
    # Step 3: Use recursion
    return fib(n-1) + fib(n-2)