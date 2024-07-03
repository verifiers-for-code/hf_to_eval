def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    

    Action Plan:
    1. Define a function `greatest_common_divisor` that takes two integers `a` and `b` as input.
    2. Implement the Euclidean algorithm:
        a. Check if `b` is 0. If true, return `a` as the GCD.
        b. If `b` is not 0, recursively call the function with `b` and the remainder of `a` divided by `b`.
    3. Handle the base case:
        a. If `b` is 0, return `a` as the GCD.
    4. Perform the recursive step:
        a. Call the function with `b` and the remainder of `a` divided by `b`.
    5. Return the final result, which is the GCD of `a` and `b`.
    
    Note: Use a recursive function to implement the Euclidean algorithm.
    Be careful with the base case and recursive step to ensure correct calculation of the GCD."""
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)