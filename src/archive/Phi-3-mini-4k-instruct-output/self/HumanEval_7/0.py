from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    # Step 2: Implement list comprehension to iterate over each string in the list
    # Step 3: Create a condition in the list comprehension to determine inclusion based on the presence of the substring
    filtered_strings = [string for string in strings if substring in string]
    
    # Step 4: Construct and return the resulting filtered list of strings
    return filtered_strings