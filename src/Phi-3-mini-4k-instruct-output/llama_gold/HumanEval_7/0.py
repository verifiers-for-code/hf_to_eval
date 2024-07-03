from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    

    Action Plan:
    1. Initialize an empty list to store the filtered strings.
    2. Iterate through each string in the input list:
       a. Check if the substring is present in the current string.
       b. If the substring is found, add the string to the filtered list.
    3. Return the filtered list containing only the strings that have the given substring."""
    
    filtered_strings = []
    for string in strings:
        if substring in string:
            filtered_strings.append(string)
    return filtered_strings