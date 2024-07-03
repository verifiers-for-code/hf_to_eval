def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # Step 1: Initialize an empty result string
    result = ''

    # Step 2: Iterate over each character in the input string
    for char in string:
        # Step 2a: Check if the character is an alphabetic character
        if char.isalpha():
            # Step 2b: Convert lowercase to uppercase and uppercase to lowercase
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            # If the character is not an alphabetic character, append it as is
            result += char

    # Step 3: Return the result string
    return result