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
    1. Extract the unit digit from the first input integer by finding the remainder when divided by 10.
    2. Extract the unit digit from the second input integer by finding the remainder when divided by 10.
    3. Take the absolute value of both unit digits to handle negative input integers.
    4. Multiply the two unit digits together.
    5. Return the product of the unit digits."""
    
    # Extract the unit digit from the first input integer
    unit_digit_a = a % 10
    
    # Extract the unit digit from the second input integer
    unit_digit_b = b % 10
    
    # Take the absolute value of both unit digits
    unit_digit_a = abs(unit_digit_a)
    unit_digit_b = abs(unit_digit_b)
    
    # Multiply the two unit digits together
    product = unit_digit_a * unit_digit_b
    
    # Return the product of the unit digits
    return product