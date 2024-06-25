def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    # Initialize the first three FibFib numbers
    fib_fib_0, fib_fib_1, fib_fib_2 = 0, 0, 1

    # Compute the n-th FibFib number
    for i in range(3, n+1):
        fib_fib = fib_fib_0 + fib_fib_1 + fib_fib_2
        fib_fib_0, fib_fib_1, fib_fib_2 = fib_fib_1, fib_fib_2, fib_fib

    return fib_fib_2