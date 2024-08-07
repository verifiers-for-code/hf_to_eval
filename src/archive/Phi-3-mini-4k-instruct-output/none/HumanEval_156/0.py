def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    # Mapping of integers to their corresponding roman numerals
    roman_map = {
        1000: 'm',
        900: 'cm',
        500: 'd',
        400: 'cd',
        100: 'c',
        90: 'xc',
        50: 'l',
        40: 'xl',
        10: 'i',
        9: 'ix',
        5: 'v',
        4: 'iv',
        1: 'i'
    }

    roman_numeral = ''

    # Iterate through the roman_map in descending order
    for value, numeral in sorted(roman_map.items(), reverse=True):
        # While the number is greater than or equal to the current value
        while number >= value:
            # Append the corresponding numeral to the roman_numeral string
            roman_numeral += numeral
            # Subtract the value from the number
            number -= value

    return roman_numeral