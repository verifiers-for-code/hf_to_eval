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
    1. Define two lists: one for decimal values (1, 4, 5, 9, 10, ...) and another for their corresponding roman numerals ("I", "IV", "V", "IX", "X", ...).
    2. Initialize an empty result string to store the roman numeral equivalent.
    3. Iterate through the decimal values in descending order:
       a. Calculate how many times the current decimal value fits into the input number.
       b. Add the corresponding roman numeral to the result string that many times.
       c. Subtract the value of the added roman numerals from the input number.
    4. Continue step 3 until the input number becomes 0.
    5. Return the result string in lowercase."""

    # Define the decimal values and their corresponding roman numerals
    decimal_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    # Initialize an empty result string
    result = ""

    # Iterate through the decimal values in descending order
    for i in range(len(decimal_values)):
        # Calculate how many times the current decimal value fits into the input number
        count = number // decimal_values[i]

        # Add the corresponding roman numeral to the result string that many times
        result += roman_numerals[i] * count

        # Subtract the value of the added roman numerals from the input number
        number -= count * decimal_values[i]

    # Return the result string in lowercase
    return result.lower()