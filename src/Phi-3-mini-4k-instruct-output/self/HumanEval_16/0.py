def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Normalize the string to ensure case-insensitivity
    normalized_string = string.lower()
    
    # Initialize an empty set to store distinct characters
    distinct_characters = set()
    
    # Iterate over each character in the normalized string
    for char in normalized_string:
        # For each character, add it to the set of distinct characters
        distinct_characters.add(char)
    
    # After iterating over all characters, count the number of elements in the set
    # This count represents the number of distinct characters in the original string
    count = len(distinct_characters)
    
    # Return the count as the result
    return count