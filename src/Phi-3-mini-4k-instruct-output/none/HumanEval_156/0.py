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
    # Define the roman numeral symbols and their corresponding values
    roman_numerals = [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1)
    ]

    # Initialize the result string
    result = ""

    # Iterate through the roman numeral symbols
    for numeral, value in roman_numerals:
        # Calculate the number of times the current symbol can be used
        count = number // value

        # Add the current symbol to the result string the appropriate number of times
        result += numeral * count

        # Update the number to reflect the remaining value
        number %= value

    # Return the result string in lowercase
    return result.lower()