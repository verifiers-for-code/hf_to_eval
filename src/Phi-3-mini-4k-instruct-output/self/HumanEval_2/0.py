def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    

    Action Plan:
    1. Validate input:
        a. Ensure the input number is a positive floating-point number
    
    2. Extract integer part:
        a. Use the int() function to obtain the integer part
    
    3. Calculate decimal part:
        a. Subtract the integer part from the original number
    
    4. Return the decimal part:
        a. Ensure the output is the decimal part
    
    5. Handle rounding and precision considerations:
        a. Consider float accuracy limitations
    
    6. Test the function with the given test cases and additional inputs to validate functionality"""

    # Validate input
    if not isinstance(number, float) or number <= 0:
        raise ValueError("Input must be a positive floating-point number")

    # Extract integer part
    integer_part = int(number)

    # Calculate decimal part
    decimal_part = number - integer_part

    # Return the decimal part
    return decimal_part