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
    1. Create two lists:
       - One for integer values in descending order (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
       - One for corresponding Roman numeral symbols (M, CM, D, CD, C, XC, L, XL, X, IX, V, IV, I)

    2. Initialize an empty result string.

    3. Iterate through the integer values list:
       a. Divide the input number by the current integer value.
       b. If the result is not zero:
          - Append the corresponding Roman numeral symbol to the result string that many times.
          - Subtract the used portion from the input number.

    4. Repeat step 3 until the input number becomes zero.

    5. Convert the result string to lowercase.

    6. Return the final result string.
    """
    # Step 1: Create two lists
    int_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    # Step 2: Initialize an empty result string
    result = ''

    # Step 3: Iterate through the integer values list
    for i in range(len(int_values)):
        # Divide the input number by the current integer value
        quotient = number // int_values[i]

        # If the result is not zero
        if quotient > 0:
            # Append the corresponding Roman numeral symbol to the result string that many times
            result += roman_symbols[i] * quotient

            # Subtract the used portion from the input number
            number -= int_values[i] * quotient

    # Step 5: Convert the result string to lowercase
    result = result.lower()

    # Step 6: Return the final result string
    return result