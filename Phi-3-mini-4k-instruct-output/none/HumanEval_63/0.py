
    def fibfib(n: int):
        """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
        fibfib(0) == 0
        fibfib(1) == 0
        fibfib(2) == 1
        fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
        Please write a function to efficiently compute the n-th element of the fibfib number sequence.
        """
        if n == 0 or n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            a, b, c = 0, 0, 1
            for _ in range(3, n+1):
                a, b, c = b, c, a + b + c
            return c