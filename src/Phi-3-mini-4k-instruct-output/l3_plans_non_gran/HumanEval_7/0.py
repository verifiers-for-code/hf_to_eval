from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.
    
    Action Plan:
    1. Define a function `filter_by_substring` that takes a list of strings and a substring as input.
    2. Initialize an empty list to store the filtered strings.
    3. Iterate through each string in the input list:
        a. Check if the substring is present in the current string using the `in` operator.
        b. If the substring is found, add the string to the filtered list.
    4. After iterating through all strings, return the filtered list of strings.
    5. Consider using a list comprehension for a more concise implementation.
    
    Note: Be mindful of the case sensitivity of the substring search, as it is not specified in the problem.
    """
    filtered_strings = [string for string in strings if substring in string]
    return filtered_strings