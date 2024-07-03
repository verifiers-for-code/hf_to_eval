def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    
    Action Plan:
    1. Understand the problem:
       - We need to extract the decimal part of a positive floating-point number.
       - The decimal part is always smaller than 1.

    2. Consider the properties of floating-point numbers:
       - A float consists of an integer part and a decimal part.
       - The decimal part is what remains after subtracting the integer part.

    3. Think about mathematical operations:
       - Which operation can give us the remainder after division?
       - How can we use this operation to separate the decimal part?

    4. Implement the solution:
       - Use a mathematical operation that returns the remainder when the number is divided by 1.
       - This operation will effectively remove the integer part and leave only the decimal part.

    5. Return the result:
       - The result of the operation in step 4 will be the decimal part we want to return.

    6. Test the function:
       - Verify that it works correctly with the given example (3.5 should return 0.5).
       - Test with other positive floating-point numbers to ensure correctness.
    """
    return number - int(number)