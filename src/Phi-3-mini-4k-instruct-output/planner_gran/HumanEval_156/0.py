def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    

    1. Define a dictionary to map decimal values to their corresponding roman numerals:
       - Create a dictionary with keys as decimal values (1, 4, 5, 10, 100, 1000) and values as their corresponding roman numerals ('i', 'iv', 'v', 'x', 'c','m')
    
    2. Initialize an empty string to store the roman numeral:
       - Create an empty string variable to store the resulting roman numeral
    
    3. Iterate through the dictionary in descending order:
       - Use a loop to iterate through the dictionary items in descending order (1000, 100, 10, 5, 4, 1)
    
    4. Check if the decimal value is less than or equal to the input number:
       - Inside the loop, check if the current decimal value is less than or equal to the input number
    
    5. Append the corresponding roman numeral to the result string:
       - If the condition is true, append the corresponding roman numeral to the result string
    
    6. Subtract the decimal value from the input number:
       - Subtract the current decimal value from the input number
    
    7. Return the final roman numeral string in lowercase:
       - After the loop, return the resulting roman numeral string in lowercase
    
    Additional implementation details:
    - Use a for loop to iterate through the dictionary items
    - Use an if statement to check the condition and append the roman numeral
    - Use the string concatenation operator (+) to append the roman numeral to the result string
    - Ensure that the function handles input values within the specified range (1 to 1000) correctly"""
    
    # Step 1: Define a dictionary to map decimal values to their corresponding roman numerals
    roman_numerals = {1000: 'm', 900: 'cm', 500: 'd', 400: 'cd', 100: 'c', 90: 'xc', 50: 'l', 40: 'xl', 10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'}
    
    # Step 2: Initialize an empty string to store the roman numeral
    roman_numeral = ''
    
    # Step 3: Iterate through the dictionary in descending order
    for decimal_value, roman_numeral_value in roman_numerals.items():
        # Step 4: Check if the decimal value is less than or equal to the input number
        while decimal_value <= number:
            # Step 5: Append the corresponding roman numeral to the result string
            roman_numeral += roman_numeral_value
            
            # Step 6: Subtract the decimal value from the input number
            number -= decimal_value
    
    # Step 7: Return the final roman numeral string in lowercase
    return roman_numeral