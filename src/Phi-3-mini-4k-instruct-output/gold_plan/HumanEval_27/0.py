def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    
    Action Plan:
    1. Initialize an empty result string to store the flipped characters.
    2. Iterate through each character in the input string:
        a. If the character is lowercase, convert it to uppercase.
        b. If the character is uppercase, convert it to lowercase.
        c. If the character is neither (e.g., numbers or symbols), keep it as is.
    3. Append each processed character to the result string.
    4. After processing all characters, return the result string.
    
    Note: Consider using string methods to check character case and perform conversions.
    """
    result = ""
    for char in string:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result