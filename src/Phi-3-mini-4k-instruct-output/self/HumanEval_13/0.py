def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Step 2: Initialize the variables
    temp = a % b
    gcd = 1

    # Step 3: Implement a loop to continue the process until the remainder is 0
    while temp != 0:
        a, b = b, temp
        temp = a % b

    # Step 4: After the loop, a will hold the GCD
    gcd = b

    # Step 5: Handle edge cases
    if a == 0:
        return b
    elif b == 0:
        return a

    # Step 7: Optimization
    # Avoid dividing by zero at any point

    # Step 8: Test the implementation with the provided test cases and potential edge cases
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(0, 5) == 5
    assert greatest_common_divisor(5, 0) == 5

    return gcd