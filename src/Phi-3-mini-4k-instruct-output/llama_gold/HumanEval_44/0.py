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
    1. Understand that the input number x needs to be converted to a different base (less than 10).
    2. Choose a suitable approach for base conversion, such as repeated division and modulo operations.
    3. Initialize an empty result string to store the converted number.
    4. Perform the base conversion using a loop:
       a. Calculate the remainder of x divided by the base.
       b. Prepend the remainder (as a string) to the result string.
       c. Update x by performing integer division by the base.
       d. Repeat steps a-c until x becomes 0.
    5. Return the result string, which now represents the input number in the desired base."""
    
    result = ""
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x = x // base
    return result