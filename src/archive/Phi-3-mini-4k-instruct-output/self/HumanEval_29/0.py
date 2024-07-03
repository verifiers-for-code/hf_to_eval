from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    # Step 1: Define the main function and parameters
    # Step 2: Handle empty input list
    if not strings:
        return []

    # Step 3: Implement list filtering logic
    filtered_strings = [string for string in strings if string.startswith(prefix)]

    # Step 4: Populate the new list with filtered strings

    # Step 5: Return the new list
    return filtered_strings