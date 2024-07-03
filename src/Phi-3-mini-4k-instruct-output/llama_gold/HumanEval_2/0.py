def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    

    Action Plan:
    1. Understand that the goal is to extract the decimal part of a given positive floating-point number.
    2. Recognize that the decimal part can be obtained by finding the remainder of the number when divided by 1.
    3. Apply the modulo operation to the input number to get the decimal part.
    4. Return the result, which is the decimal part of the original number.
    
    Note: The modulo operation (%) is used to find the remainder of the division of the number by 1, effectively giving the decimal part."""

    # Step 1: Understand the problem
    # The goal is to extract the decimal part of a given positive floating-point number.

    # Step 2: Recognize the solution
    # The decimal part can be obtained by finding the remainder of the number when divided by 1.

    # Step 3: Apply the modulo operation
    decimal_part = number % 1

    # Step 4: Return the result
    return decimal_part