def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Step 1: Validate input
    if not isinstance(number, float) or number <= 0:
        raise ValueError("Input must be a positive floating-point number")

    # Step 2: Extract integer part
    integer_part = int(number)

    # Step 3: Calculate decimal part
    decimal_part = number - integer_part

    # Step 4: Return the decimal part
    return decimal_part