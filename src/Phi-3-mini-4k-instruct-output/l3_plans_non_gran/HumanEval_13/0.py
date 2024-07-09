def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    

    Action Plan:
    1. Understand the problem: The goal is to find the greatest common divisor (GCD) of two integers a and b.
    2. Initialize variables: Set up two variables, x and y, to store the values of a and b, respectively.
    3. Implement the Euclidean algorithm loop:
        a. Calculate the remainder of x divided by y and store it in x.
        b. Calculate the remainder of y divided by x and store it in y.
        c. Repeat steps a and b until y becomes 0.
    4. Return the final result: The GCD is the last non-zero value of x.
    5. Consider edge cases: Handle the case where a or b is 0.
    
    Note: The Euclidean algorithm is an efficient method for finding the GCD of two numbers. It works by repeatedly dividing the larger number by the smaller number and taking the remainder, until the remainder is 0."""
    if a == 0:
        return b
    if b == 0:
        return a
    while b != 0:
        x, y = y, a % y
    return x