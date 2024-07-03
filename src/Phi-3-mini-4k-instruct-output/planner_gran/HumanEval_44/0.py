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
    

    1. Initialize an empty string to store the converted number
       - This string will hold the digits of the converted number
    
    2. Check if the base is less than 10:
       - If true, proceed with the conversion
       - If false, return an error message or handle it according to the problem requirements
    
    3. While the input number is greater than 0:
       a. Calculate the remainder of the number when divided by the base
       b. Convert the remainder to a string
       c. Prepend the string to the front of the converted number string
       d. Update the input number by performing integer division by the base
    
    4. Return the final converted number string
    
    Additional implementation details:
    - Use the modulo operator (%) to calculate the remainder of the number when divided by the base
    - Use the floor division operator (//) to perform integer division of the number by the base
    - Use string concatenation to prepend the remainder string to the converted number string
    - Ensure that the function handles edge cases, such as an input number of 0 or a base of 1
    - Consider adding error handling for invalid input values (e.g., base less than 1 or non-integer input numbers)"""
    if base < 2 or base > 10:
        return "Error: Base must be between 2 and 10."
    if not isinstance(x, int) or not isinstance(base, int):
        return "Error: Inputs must be integers."
    if x == 0:
        return "0"
    converted_number = ""
    while x > 0:
        remainder = x % base
        converted_number = str(remainder) + converted_number
        x = x // base
    return converted_number