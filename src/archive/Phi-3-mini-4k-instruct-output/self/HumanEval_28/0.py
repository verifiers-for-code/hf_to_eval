from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # Step 1: Initialize the concatenation result as an empty string
    result = ''

    # Step 2: Use a loop to iterate through each string in the input list
    for string in strings:
        # Step 3: Within the loop, add each string to the concatenation result
        result += string

    # Step 4: Handle edge cases
    # a. Empty input list
    if not strings:
        return result

    # b. List with one or no strings
    if len(strings) <= 1:
        return strings[0] if strings else ''

    # Step 5: Optionally, add comments explaining each step to aid in clarity and understanding
    # The function concatenates all strings in the input list into a single string
    # If the input list is empty, it returns an empty string
    # If the input list contains one or no strings, it returns the single string (or an empty string if the list is empty)

    return result