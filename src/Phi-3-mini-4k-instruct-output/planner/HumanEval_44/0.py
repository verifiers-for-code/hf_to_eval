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
    1. Define the function `change_base` with two parameters: `x` (the input number) and `base` (the desired base).
    2. Initialize an empty string `result` to store the converted number.
    3. Implement a loop that continues until `x` becomes 0.
    4. Inside the loop:
        a. Calculate the remainder of `x` divided by `base` using the modulo operator (%).
        b. Convert the remainder to a string and prepend it to the `result` string.
        c. Update `x` by performing integer division by `base` using the floor division operator (//).
    5. After the loop, return the `result` string, which represents the input number `x` in the desired base.
    6. Consider handling potential edge cases, such as invalid input values for `x` or `base`.
    """
    result = ""
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x = x // base
    return result