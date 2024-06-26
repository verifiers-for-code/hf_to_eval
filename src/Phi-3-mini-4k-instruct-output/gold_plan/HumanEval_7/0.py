from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    
    Action Plan:
    1. Initialize an empty list to store the filtered strings.
    2. Iterate through each string in the input 'strings' list.
    3. For each string, check if the 'substring' is present in it.
    4. If the substring is found, add the current string to the filtered list.
    5. After checking all strings, return the filtered list.
    
    Note: Consider using a list comprehension for a more concise implementation.
    """
    return [string for string in strings if substring in string]