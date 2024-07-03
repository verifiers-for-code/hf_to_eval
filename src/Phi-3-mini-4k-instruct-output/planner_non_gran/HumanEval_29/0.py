from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    

    Action Plan:
    1. Define the function with two parameters: strings (a list of strings) and prefix (a string).
    2. Initialize an empty list to store the filtered strings.
    3. Iterate through each string in the input list:
        a. Check if the current string starts with the given prefix using the `startswith` method.
        b. If the string starts with the prefix, add it to the filtered list.
    4. After iterating through all strings, return the filtered list.
    5. Consider using a list comprehension for a more concise implementation.
    
    Note: Be mindful of the function's purpose and the expected output."""
    return [string for string in strings if string.startswith(prefix)]