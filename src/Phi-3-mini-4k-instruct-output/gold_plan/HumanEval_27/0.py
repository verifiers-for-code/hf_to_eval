def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # Step 1: Initialize an empty result string
    result = ''

    # Step 2: Iterate through each character in the input string
    for char in string:
        # Step 2a: Check if the character is lowercase
        if char.islower():
            # Convert it to uppercase and append to result
            result += char.upper()
        # Step 2b: Check if the character is uppercase
        elif char.isupper():
            # Convert it to lowercase and append to result
            result += char.lower()
        # Step 2c: If the character is neither (e.g., numbers or symbols), keep it as is
        else:
            result += char

    # Step 3: Return the result string
    return result