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
    1. Create a dictionary to map integers to their corresponding Roman numerals.
    2. Initialize an empty string to store the Roman numeral.
    3. Iterate through the dictionary in descending order of the integers.
    4. For each integer, calculate the number of times it can be used in the Roman numeral:
        a. Divide the input number by the current integer.
        b. Append the corresponding Roman numeral to the result string, repeated the calculated number of times.
        c. Update the input number by subtracting the product of the current integer and the calculated number.
    5. After iterating through all integers, return the final Roman numeral string in lowercase.
    6. Consider handling edge cases, such as input numbers outside the specified range (1 to 1000).
    """
    # Step 1: Create a dictionary to map integers to their corresponding Roman numerals
    roman_numerals = {
        1000: 'm',
        900: 'cm',
        500: 'd',
        400: 'cd',
        100: 'c',
        90: 'xc',
        50: 'l',
        40: 'xl',
        10: 'x',
        9: 'ix',
        5: 'v',
        4: 'iv',
        1: 'i'
    }

    # Step 2: Initialize an empty string to store the Roman numeral
    roman_numeral = ''

    # Step 3: Iterate through the dictionary in descending order of the integers
    for value, numeral in sorted(roman_numerals.items(), reverse=True):
        # Step 4: Calculate the number of times the current integer can be used in the Roman numeral
        count = number // value

        # Append the corresponding Roman numeral to the result string, repeated the calculated number of times
        roman_numeral += numeral * count

        # Update the input number by subtracting the product of the current integer and the calculated number
        number %= value

    # Step 5: Return the final Roman numeral string in lowercase
    return roman_numeral.lower()