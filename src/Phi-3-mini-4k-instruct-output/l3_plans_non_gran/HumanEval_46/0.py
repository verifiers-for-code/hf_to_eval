def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    

    Action Plan:
    1. Define the function `fib4` with a single parameter `n`.
    2. Initialize an array `fib` of size `n + 1` with all elements set to 0.
    3. Set `fib[0]`, `fib[1]`, and `fib[2]` to 0, 0, and 2, respectively.
    4. Implement a loop that iterates from 3 to `n` (inclusive):
        a. Calculate the `i`-th element of the sequence by summing the previous four elements (`fib[i-1]`, `fib[i-2]`, `fib[i-3]`, and `fib[i-4]`).
        b. Store the result in `fib[i]`.
    5. Return the `n`-th element of the sequence, which is stored in `fib[n]`.
    6. Consider optimizing the function for performance, if necessary."""
    fib = [0] * (n + 1)
    fib[0] = fib[1] = 0
    fib[2] = 2
    for i in range(3, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2] + fib[i - 3] + fib[i - 4]
    return fib[n]