def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    

    1. Understand the GCD concept:
       - The GCD of two numbers is the largest number that divides both numbers without leaving a remainder
    
    2. Implement the Euclidean algorithm:
       - Start with the input numbers a and b
       - While b is not zero:
         a. Calculate the remainder of a divided by b (a % b)
         b. Update a to be the current value of b
         c. Update b to be the remainder calculated in step 2a
       - When b becomes zero, the GCD is the final value of a
    
    3. Handle edge cases:
       - If a or b is zero, the GCD is the non-zero value (or zero if both are zero)
       - Ensure the function returns the correct result for these cases
    
    4. Optimize the algorithm:
       - The Euclidean algorithm is an efficient way to calculate the GCD
       - No further optimization is needed, as the algorithm is already efficient
    
    5. Return the GCD:
       - Once the loop terminates (b is zero), return the final value of a, which is the GCD of the original a and b
    
    Additional implementation details:
    - Use a while loop to implement the Euclidean algorithm
    - Use the modulus operator (%) to calculate the remainder
    - Update the values of a and b correctly in each iteration
    - Ensure the function handles negative input values correctly (GCD is always positive)"""
    if a == 0:
        return b
    if b == 0:
        return a
    while b != 0:
        a, b = b, a % b
    return abs(a)