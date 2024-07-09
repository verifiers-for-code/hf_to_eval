from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    

    Action Plan:
    1. Define the function `filter_by_prefix` with two parameters: `strings` (a list of strings) and `prefix` (a string).
    2. Initialize an empty list `filtered_strings` to store the filtered strings.
    3. Iterate through each string in the `strings` list:
        a. Check if the string starts with the `prefix` using the `startswith` method.
        b. If the string matches the prefix, add it to the `filtered_strings` list.
    4. After iterating through all strings, return the `filtered_strings` list.
    5. Consider edge cases, such as an empty input list or a prefix that matches all strings.
    
    Note: Use a list comprehension or a for loop to iterate through the strings and filter the results.
    Be mindful of the `startswith` method's behavior and how it handles case sensitivity."""
    filtered_strings = [string for string in strings if string.startswith(prefix)]
    return filtered_strings