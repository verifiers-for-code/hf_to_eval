def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Implement the Euclidean algorithm for finding GCD
    while b != 0:
        # Assign the value of b to a temporary variable
        temp = b
        # Update b to be the remainder of a divided by b
        b = a % b
        # Assign the temporary variable's value to a
        a = temp
    # After the loop ends, return the final value of a as the GCD
    return a