def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    >>> truncate_number(3.5)
    0.5

    Action Plan:
    1. Understand the problem:
        - The function takes a positive floating point number as input
        - The goal is to return the decimal part of the number
    
    2. Identify the key operation:
        - Truncate the number to remove the integer part
        - This can be done by subtracting the integer part from the original number
    
    3. Implement the truncation logic:
        - Use the `int()` function to get the integer part of the number
        - Subtract the integer part from the original number to get the decimal part
    
    4. Return the decimal part:
        - The result of the subtraction is the decimal part of the number
        - Return this value as the output of the function
    
    Note: Be careful with the subtraction operation to ensure it returns the correct decimal part.
    """
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part