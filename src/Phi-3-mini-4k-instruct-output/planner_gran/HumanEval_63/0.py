def fibfib(n: int, cache: dict = {0: 0, 1: 0, 2: 1}) -> int:
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    
    Action Plan:
    1. Define the function `fibfib` with a single parameter `n` of type `int`
       - This function will compute the n-th element of the FibFib number sequence
    
    2. Handle the base cases:
       a. If `n` is 0, return 0 (the 0-th element of the sequence)
       b. If `n` is 1, return 0 (the 1-th element of the sequence)
       c. If `n` is 2, return 1 (the 2-th element of the sequence)
    
    3. Implement the recursive formula for `n` > 2:
       a. Calculate `fibfib(n-1)` (the (n-1)-th element of the sequence)
       b. Calculate `fibfib(n-2)` (the (n-2)-th element of the sequence)
       c. Calculate `fibfib(n-3)` (the (n-3)-th element of the sequence)
       d. Return the sum of these three elements
    
    4. Optimize the function for efficiency:
       - Consider using memoization or dynamic programming to avoid redundant calculations
       - Store the computed values in a cache or table to reuse them for future calculations
    
    5. Test the function with various inputs to ensure it produces the correct results
       - Use the provided unit tests as a starting point
       - Verify that the function handles edge cases correctly (e.g., `n = 0`, `n = 1`, `n = 2`)
    
    By following this plan, a model should be able to implement the `fibfib` function correctly and efficiently."""
    
    if n in cache:
        return cache[n]
    else:
        cache[n] = fibfib(n-1, cache) + fibfib(n-2, cache) + fibfib(n-3, cache)
        return cache[n]