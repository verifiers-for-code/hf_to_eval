def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    

    Action Plan:
    1. Define what a prime number is: a number greater than 1 with no divisors other than 1 and itself.
    2. Handle the edge case: if `n` is 1, it's not prime, so return `y`.
    3. Iterate from 2 to `n-1` to check for divisors:
       a. If `n` is divisible by any number in this range, it's not prime, so return `y`.
       b. If no divisors are found, `n` is prime, so return `x`.
    4. Implement the iteration and conditional checks to determine whether to return `x` or `y`."""

    # Handle the edge case
    if n == 1:
        return y

    # Check for divisors
    for i in range(2, n):
        if n % i == 0:
            return y

    # If no divisors found, n is prime
    return x