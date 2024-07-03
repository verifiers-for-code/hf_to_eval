def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # Step 1: Initialize variables to track the previous two Fibonacci numbers
    fib_prev = 0
    fib_current = 1

    # Step 2: Create a loop to iterate n times
    for _ in range(2, n + 1):
        # At each iteration, calculate the next Fibonacci number
        fib_next = fib_prev + fib_current

        # Update fib_prev and fib_current
        fib_prev = fib_current
        fib_current = fib_next

    # Step 3: Return fib_current, which represents the n-th Fibonacci number after the loop
    return fib_current


# Step 4: Edge cases
def fib_edge_cases(n: int):
    if n < 1:
        return fib_current
    elif n == 0:
        return fib_prev
    else:
        return fib(n)


# Step 5: Alternative approaches
def fib_recursive(n: int):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def fib_memoization(n: int, memo={}):
    if n in memo:
        return memo[n]
    elif n <= 1:
        return n
    else:
        memo[n] = fib_memoization(n-1, memo) + fib_memoization(n-2, memo)
        return memo[n]