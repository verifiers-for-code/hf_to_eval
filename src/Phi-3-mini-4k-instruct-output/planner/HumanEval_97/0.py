def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    

    Action Plan:
    1. Define the function `multiply` with two integer parameters `a` and `b`.
    2. Extract the unit digits of `a` and `b` by using the modulo operator `%` with 10.
    3. Multiply the unit digits of `a` and `b` using the `*` operator.
    4. Return the result of the multiplication.
    5. No need for error handling as the problem assumes valid input.
    
    Note: The problem statement specifies that the input is always valid, so no error handling is required."""
    
    # Extract the unit digits of a and b
    unit_digit_a = a % 10
    unit_digit_b = b % 10
    
    # Multiply the unit digits
    result = unit_digit_a * unit_digit_b
    
    # Return the result
    return result