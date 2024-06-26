def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    """
    # Step 1: Handle the base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1

    # Step 2: Implement the recursive formula
    # Step 3: Efficiency improvements
    # Using memoization
    memo = {0: 0, 1: 0, 2: 1}

    def fibfib_memo(n):
        if n not in memo:
            memo[n] = fibfib_memo(n-1) + fibfib_memo(n-2) + fibfib_memo(n-3)
        return memo[n]

    return fibfib_memo(n)