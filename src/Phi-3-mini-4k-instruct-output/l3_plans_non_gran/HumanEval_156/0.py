def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    

    Action Plan:
    1. Define a function `int_to_mini_roman` that takes an integer `number` as input.
    2. Create a dictionary `roman_numerals` that maps integers to their corresponding roman numerals (e.g., 1: 'i', 2: 'ii', 3: 'iii',..., 9: 'ix', 10: 'x', 20: 'xx', 30: 'xxx',..., 90: 'xc', 100: 'c', 200: 'cc', 300: 'ccc',..., 900: 'cm', 1000:'m').
    3. Initialize an empty string `roman` to store the constructed roman numeral.
    4. Implement a loop that continues until `number` becomes 0:
        a. Find the largest roman numeral in `roman_numerals` that is less than or equal to `number`.
        b. Append the corresponding roman numeral to the `roman` string.
        c. Subtract the value of the appended roman numeral from `number`.
    5. Convert the `roman` string to lowercase using the `lower()` method.
    6. Return the final `roman` string."""

    roman_numerals = {
        1: 'i', 2: 'ii', 3: 'iii', 4: 'iv', 5: 'v', 6: 'vi', 7: 'vii', 8: 'viii', 9: 'ix',
        10: 'x', 20: 'xx', 30: 'xxx', 40: 'xl', 50: 'l', 60: 'lx', 70: 'lxx', 80: 'lxxx', 90: 'xc',
        100: 'c', 200: 'cc', 300: 'ccc', 400: 'cd', 500: 'd', 600: 'dc', 700: 'dcc', 800: 'dccc', 900: 'cm',
        1000: 'm'
    }

    roman = ""
    for key in sorted(roman_numerals.keys(), reverse=True):
        while number >= key:
            roman += roman_numerals[key]
            number -= key

    return roman.lower()