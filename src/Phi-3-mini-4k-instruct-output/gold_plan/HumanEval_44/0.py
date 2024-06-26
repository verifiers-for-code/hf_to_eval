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
    """
    # Step 1: Initialize an empty string to store the result
    result = ""

    # Step 2: Enter a loop that continues while x is greater than 0
    while x > 0:
        # a. Calculate the remainder when x is divided by the new base
        remainder = x % base

        # b. Convert this remainder to a string and add it to the left side of the result string
        result = str(remainder) + result

        # c. Update x by integer dividing it by the new base
        x = x // base

    # Step 3: After the loop ends, return the result string
    return result