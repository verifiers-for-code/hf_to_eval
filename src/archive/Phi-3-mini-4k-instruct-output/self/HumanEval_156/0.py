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
    # Step 1: Initialize a dictionary for mapping each digit to its corresponding Roman numeral
    roman_numerals = {
        1: 'i', 2: 'ii', 3: 'iii', 4: 'iv', 5: 'v', 6: 'vi', 7: 'vii', 8: 'viii', 9: 'ix',
        10: 'x', 20: 'xx', 30: 'xxx', 40: 'xl', 50: 'l', 60: 'lx', 70: 'lxx', 80: 'lxxx', 90: 'xc',
        100: 'cc', 200: 'ccx', 300: 'ccc', 400: 'cd', 500: 'd', 600: 'dcl', 700: 'dccc', 800: 'dccc', 900: 'cm'
    }

    # Step 2: Validate the input to ensure it's within the required range (1 to 1000)
    if not 1 <= number <= 1000:
        raise ValueError("Input must be between 1 and 1000.")

    # Step 3: Break the input number into its individual digits
    number_str = str(number)[::-1]

    # Step 4: Iterate over each digit in reverse, convert it to its Roman numeral equivalent
    roman_numeral = ''
    for i, digit in enumerate(number_str):
        value = int(digit)
        numeral = roman_numerals[value]
        roman_numeral += numeral * (10 ** i)

    # Step 5: Return the constructed Roman numeral string in lowercase
    return roman_numeral.lower()