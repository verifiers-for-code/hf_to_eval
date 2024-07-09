def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    

    Action Plan:
    1. Validate the input base:
        - Check if the base is less than 10
        - Raise a ValueError if the base is not valid
    
    2. Initialize an empty string to store the result
    
    3. Implement a loop to convert the input number to the desired base:
        - Use a while loop to repeatedly divide the input number by the base
        - Extract the remainder of the division (using the modulus operator)
        - Prepend the remainder to the result string
        - Update the input number for the next iteration
    
    4. Return the final result as a string
    
    Note: Be careful with the order of operations and the handling of the remainder in each iteration.
    Consider using a recursive approach as an alternative to the loop."""
    
    # Validate the input base
    if base < 2 or base > 10:
        raise ValueError("Base must be between 2 and 10")
    
    # Initialize an empty string to store the result
    result = ""
    
    # Implement a loop to convert the input number to the desired base
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x = x // base
    
    # Return the final result as a string
    return result