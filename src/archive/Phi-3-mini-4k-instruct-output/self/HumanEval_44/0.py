def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    # Step 1: Define the function signature with x (integer) and base (base-10 number less than 10) parameters
    if not 2 <= base < 11:
        return "Error: Base must be a number less than 10 and greater than or equal to 2."
    
    result = ""
    
    # Step 2: Initialize an empty string variable to store the result
    # Step 3: Handle edge cases
    if x == 0:
        return '0'
    
    # Step 4: Implement a while-loop that runs until x becomes 0
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x = x // base
    
    # Step 5: Reverse the result string to get the correct base representation
    return result