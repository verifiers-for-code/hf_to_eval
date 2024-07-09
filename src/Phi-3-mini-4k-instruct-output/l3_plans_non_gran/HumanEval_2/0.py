def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    

    Action Plan:
    1. Define the function `truncate_number` with a single parameter `number` of type `float`.
    2. Decompose the input `number` into its integer part and decimal part using the `int()` and `float()` functions.
    3. Extract the decimal part by subtracting the integer part from the original `number`.
    4. Return the decimal part as a `float` value.
    
    Note: Ensure the function works correctly for positive floating-point numbers."""
    
    # Step 1: Define the function `truncate_number` with a single parameter `number` of type `float`.
    def truncate_number(number: float) -> float:
        # Step 2: Decompose the input `number` into its integer part and decimal part using the `int()` and `float()` functions.
        integer_part = int(number)
        decimal_part = number - integer_part
        
        # Step 3: Extract the decimal part by subtracting the integer part from the original `number`.
        # Step 4: Return the decimal part as a `float` value.
        return decimal_part