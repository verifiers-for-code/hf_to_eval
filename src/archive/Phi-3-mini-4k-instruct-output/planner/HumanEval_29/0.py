from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    Args:
    strings (List[str]): A list of strings to be filtered.
    prefix (str): The prefix to filter the strings by.

    Returns:
    List[str]: A list of strings that start with the given prefix.

    Examples:
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    # Step 2: Initialize an empty list to store the filtered strings
    filtered_strings = []

    # Step 3: Iterate through each string in the input list
    for string in strings:
        # Step 3a: Check if the current string starts with the given prefix
        if string.startswith(prefix):
            # Step 3b: Add the string to the filtered list
            filtered_strings.append(string)

    # Step 4: Return the filtered list
    return filtered_strings

# Using list comprehension for a more concise implementation
def filter_by_prefix_comprehension(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix using list comprehension.

    Args:
    strings (List[str]): A list of strings to be filtered.
    prefix (str): The prefix to filter the strings by.

    Returns:
    List[str]: A list of strings that start with the given prefix.

    Examples:
    >>> filter_by_prefix_comprehension([], 'a')
    []
    >>> filter_by_prefix_comprehension(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    # Step 4: Return the filtered list using list comprehension
    return [string for string in strings if string.startswith(prefix)]