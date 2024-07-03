def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5

    Action Plan:
    1. Define a helper function `is_prime(n)` to check if a number `n` is prime:
        a. Handle edge cases: 0, 1, and negative numbers
        b. Iterate from 2 to the square root of `n` to check for divisors
        c. Return `True` if no divisors are found, `False` otherwise
    
    2. Define the main function `x_or_y(n, x, y)`:
        a. Call the `is_prime(n)` function to check if `n` is prime
        b. If `n` is prime, return `x`
        c. If `n` is not prime, return `y`
    
    3. Implement the `is_prime(n)` function:
        a. Handle edge cases: 0, 1, and negative numbers
        b. Iterate from 2 to the square root of `n` to check for divisors
        c. Return `True` if no divisors are found, `False` otherwise
    
    4. Use the `is_prime(n)` function in the `x_or_y(n, x, y)` function to determine the return value based on the primality of `n`

    Note: Be careful with the implementation of the `is_prime(n)` function to ensure it correctly identifies prime numbers.
    """
    def is_prime(n):
        """Check if a number is prime.

        Args:
        n (int): The number to check.

        Returns:
        bool: True if the number is prime, False otherwise.
        """
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if is_prime(n):
        return x
    else:
        return y