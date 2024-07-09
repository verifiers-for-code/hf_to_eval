def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    

    Action Plan:
    1. Define the function `fib` that takes an integer `n` as input.
    2. Handle base cases:
        - If `n` is 1 or 0, return 1 (the first two Fibonacci numbers).
    3. Initialize variables:
        - `a` and `b` to store the last two Fibonacci numbers.
        - Set `a` to 1 and `b` to 1.
    4. Implement the recursive logic:
        - Iterate `n-1` times:
            a. Update `a` and `b` to the next two Fibonacci numbers: `a, b = b, a + b`.
    5. Return the `n`-th Fibonacci number, which is `b`.
    """
    if n == 0 or n == 1:
        return 1
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b