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
    2. Extract the unit digits of `a` and `b` using the modulo operator `%`.
    3. Calculate the product of the unit digits by multiplying them together.
    4. Return the product as the result of the function.
    5. Ensure the function is properly documented with a docstring that explains its purpose, parameters, and return value."""
    
    # Extract the unit digits of `a` and `b` using the modulo operator `%`
    unit_digit_a = a % 10
    unit_digit_b = b % 10
    
    # Calculate the product of the unit digits by multiplying them together
    product = unit_digit_a * unit_digit_b
    
    # Return the product as the result of the function
    return product