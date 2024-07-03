def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5

    Action Plan:
    1. Implement the Euclidean algorithm for finding GCD:
       a. Create a loop that continues as long as b is not zero
       b. Inside the loop:
          - Assign the value of b to a temporary variable
          - Update b to be the remainder of a divided by b
          - Assign the temporary variable's value to a
    2. After the loop ends, return the final value of a as the GCD

    Note: The Euclidean algorithm states that the GCD of two numbers
    doesn't change if the smaller number is subtracted from the larger
    number. This is equivalent to using the modulo operation.
    """
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a