def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its Roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    

    Action Plan:
    1. Initialize a dictionary for mapping each digit to its corresponding Roman numeral:
        - Create numerals for 1-9, 10, 100, and 1000
    
    2. Validate the input to ensure it's within the required range (1 to 1000):
        - If not, return an error or raise an exception
    
    3. Break the input number into its individual digits:
        - Convert the number to a string and reverse it for efficient digit-by-digit processing
    
    4. Iterate over each digit in reverse, convert it to its Roman numeral equivalent:
        - Use dictionary lookups for conversion
    
    5. Construct the Roman numeral string by concatenating the converted digits:
        - Maintain the correct order to ensure proper concatenation
    
    6. Return the constructed Roman numeral string in lowercase
    
    7. Consider edge cases and exceptional scenarios:
        - Add error handling for invalid inputs
        - Include tests to confirm that the conversion adheres to the given examples
    """
    # Step 1: Initialize a dictionary for mapping each digit to its corresponding Roman numeral
    numerals = {
        1: 'i',
        4: 'iv',
        5: 'v',
        9: 'ix',
        10: 'x',
        40: 'xl',
        50: 'l',
        90: 'xc',
        100: 'c',
        400: 'cd',
        500: 'd',
        900: 'cm',
        1000: 'm'
    }

    # Step 2: Validate the input to ensure it's within the required range (1 to 1000)
    if not 1 <= number <= 1000:
        raise ValueError("Input must be between 1 and 1000")

    # Step 3: Break the input number into its individual digits
    digits = [int(digit) for digit in str(number)[::-1]]

    # Step 4: Iterate over each digit in reverse, convert it to its Roman numeral equivalent
    roman_numeral = ''
    for i, digit in enumerate(digits):
        if digit == 0:
            continue
        for numeral, value in numerals.items():
            if digit >= value:
                roman_numeral += value
                digit -= value
                break

    # Step 5: Construct the Roman numeral string by concatenating the converted digits
    # Step 6: Return the constructed Roman numeral string in lowercase
    return roman_numeral.lower()