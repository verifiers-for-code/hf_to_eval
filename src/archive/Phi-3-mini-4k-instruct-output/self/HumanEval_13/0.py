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
        gcd = b
    
    # Step 5: Handle edge cases
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Step 6: Return the GCD
    return gcd