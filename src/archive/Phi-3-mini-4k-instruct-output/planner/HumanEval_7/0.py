from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring

    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']

    Action Plan:
    1. Define the function `filter_by_substring` with two parameters: `strings` (a list of strings) and `substring` (a string to filter by).
    2. Initialize an empty list `filtered_strings` to store the strings that contain the given substring.
    3. Iterate through each string `s` in the input list `strings`:
        a. Check if the substring `substring` is present in the current string `s` using the `in` operator.
        b. If the substring is found, add the string `s` to the `filtered_strings` list.
    4. After iterating through all strings, return the `filtered_strings` list.
    5. Consider using a list comprehension to simplify the iteration and filtering process.
    
    Note: Be mindful of the case sensitivity when checking for the substring."""
    
    filtered_strings = [s for s in strings if substring in s]
    return filtered_strings