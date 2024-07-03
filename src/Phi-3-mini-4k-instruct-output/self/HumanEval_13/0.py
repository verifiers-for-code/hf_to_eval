def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    
    Action Plan:
    1. Understand the Euclidean algorithm for GCD:
        - The GCD of two numbers a and b is the same as the GCD of b and the remainder of the division of a by b
        - Repeatedly calculate the remainder and divide the original number by it until the remainder is 0
    
    2. Initialize the variables:
        - Set a temporary variable to store the remainder
        - Set the GCD to 1 as a default case
    
    3. Implement a loop to continue the process until the remainder is 0:
        - Calculate the remainder when dividing a by b
        - Swap the values of a and b if b is not zero (since the next iteration will be with a=b and b=remainder)
    
    4. After the loop, a will hold the GCD
    
    5. Handle edge cases:
        - Inputs where one of the numbers is 0
        - Ensure the input values are integers
    
    6. Return the GCD
    
    7. Optimization:
        - Avoid dividing by zero at any point
    
    8. Test the implementation with the provided test cases and potential edge cases
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Input values must be integers")
    
    if a == 0 or b == 0:
        return max(a, b)
    
    while b != 0:
        remainder = a % b
        a, b = b, remainder
    
    return a