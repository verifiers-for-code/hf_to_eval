def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    

    Action Plan:
    1. Initialize an empty result string to store the flipped case characters.
    2. Iterate through each character in the input string:
       a. Check if the character is in lowercase.
          - If true, convert it to uppercase and add to the result string.
       b. Check if the character is in uppercase.
          - If true, convert it to lowercase and add to the result string.
    3. Return the result string with all characters having their case flipped.
    Note: Consider using built-in string methods or conditional expressions to achieve the case flipping."""
    
    result = ""
    for char in string:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result