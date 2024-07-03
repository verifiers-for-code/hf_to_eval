def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    

    Action Plan:
    1. Initialize the variables a and b with the input values.
    2. Implement the Euclidean algorithm to find the GCD:
       a. While b is not zero:
          - Replace a with the current value of b
          - Replace b with the remainder of a divided by b
    3. When b becomes zero, a will hold the GCD of the original a and b.
    4. Return the value of a as the greatest common divisor."""
    
    # Step 1: Initialize the variables a and b with the input values
    a, b = a, b
    
    # Step 2: Implement the Euclidean algorithm to find the GCD
    while b != 0:
        a, b = b, a % b
    
    # Step 3: When b becomes zero, a will hold the GCD of the original a and b
    
    # Step 4: Return the value of a as the greatest common divisor
    return a