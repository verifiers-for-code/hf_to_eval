def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    

    Action Plan:
    1. Define a helper function `is_prime(n)` to check if a number `n` is prime:
        a. Handle the edge case where `n` is less than or equal to 1
        b. Iterate from 2 to the square root of `n` to check for divisibility
        c. Return `True` if `n` is not divisible by any number in the range, `False` otherwise
    
    2. Define the main function `x_or_y(n, x, y)`:
        a. Check if `n` is prime using the `is_prime(n)` function
        b. If `n` is prime, return the value of `x`
        c. If `n` is not prime, return the value of `y`
    
    3. Implement the logic to return the correct value based on the input conditions
        a. Use the `is_prime(n)` function to determine the return value
        b. Return the appropriate value (`x` or `y`) based on the result of the `is_prime(n)` function
    
    Note: Ensure the implementation of the `is_prime(n)` function is correct and efficient."""
    
    def is_prime(n):
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