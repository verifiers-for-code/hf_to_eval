def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Action Plan:
    1. Initialize an empty result string
    2. Iterate over each character in the input string:
        a. Check if the character is an alphabetic character
        b. Convert lowercase to uppercase and uppercase to lowercase
        c. Append the modified character to the result string
    3. Return the result string
    
    Example:
    >>> flip_case('Hello')
    'hELLO'
    """
    result = ""
    for char in string:
        if char.isalpha():
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char
    return result