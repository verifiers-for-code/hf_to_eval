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
    1. Initialize an empty string to store the result.
    2. Enter a loop that continues while x is greater than 0:
       a. Calculate the remainder when x is divided by the new base.
       b. Convert this remainder to a string and add it to the left side of the result string.
       c. Update x by integer dividing it by the new base.
    3. After the loop ends, return the result string.

    Key concepts to remember:
    - Use modulo (%) to get remainders
    - Use integer division (//) to update x
    - Build the string from right to left
    - Convert numbers to strings before concatenation
    """
    result = ""
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x = x // base
    return result