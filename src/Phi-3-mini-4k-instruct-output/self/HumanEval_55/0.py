def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # Initialize variables to track the previous two Fibonacci numbers
    fib_prev = 0
    fib_current = 1

    # Create a loop to iterate n times
    for _ in range(n):
        # Calculate the next Fibonacci number
        fib_next = fib_prev + fib_current

        # Update fib_prev and fib_current
        fib_prev = fib_current
        fib_current = fib_next

    # Return fib_current, which represents the n-th Fibonacci number after the loop
    return fib_current

# Testing
assert fib(10) == 55
assert fib(1) == 1
assert fib(8) == 21

# Edge cases
assert fib(0) == 0
assert fib(-1) == 1  # This is incorrect, should return 0

# Alternative approaches

# Recursion
def fib_recursive(n: int):
    if n < 0:
        return "Invalid input"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

# Memoization
def fib_memo(n: int, memo={}):
    if n in memo:
        return memo[n]
    elif n < 0:
        return "Invalid input"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
        return memo[n]