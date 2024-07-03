def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    

    1. Understand the problem:
       - The function takes a positive floating-point number as input
       - The goal is to return the decimal part of the number
    
    2. Extract the decimal part:
       - Use the modulo operator (%) to find the remainder of the number when divided by 1
       - This will give the decimal part of the number
    
    3. Return the decimal part:
       - Ensure the returned value is a float, as the decimal part can be a fraction
       - Return the extracted decimal part as the result
    
    Additional implementation details:
    - The function should handle positive floating-point numbers as input
    - The function should return a float value representing the decimal part of the input number
    - The modulo operator (%) is used to extract the remainder, which is the decimal part of the number
    - The function does not need to handle negative numbers or non-numeric input, as the problem statement specifies a positive floating-point number as input"""
    return number % 1.0