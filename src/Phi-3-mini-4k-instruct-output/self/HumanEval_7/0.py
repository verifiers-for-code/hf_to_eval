from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    # Step 2: Implement list comprehension to filter strings
    filtered_strings = [string for string in strings if substring in string]
    
    # Step 4: Return the filtered list
    return filtered_strings