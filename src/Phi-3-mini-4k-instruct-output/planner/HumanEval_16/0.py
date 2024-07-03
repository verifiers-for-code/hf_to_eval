def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    

    Action Plan:
    1. Convert the input string to lowercase to ensure case-insensitive comparison.
    2. Create an empty set to store distinct characters.
    3. Iterate through each character in the lowercase string:
        a. Add the character to the set (duplicate characters will be ignored).
    4. Return the size of the set, which represents the number of distinct characters in the input string.
    
    Note: Use a set to automatically handle duplicates and ensure case-insensitive comparison."""
    string = string.lower()
    distinct_characters = set()
    for char in string:
        distinct_characters.add(char)
    return len(distinct_characters)