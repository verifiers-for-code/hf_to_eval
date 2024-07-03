def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.
    
    Action Plan:
    1. Normalize the string to ensure case-insensitivity:
        a. Convert the string to lower case
    
    2. Initialize an empty set to store distinct characters:
        a. A set automatically removes duplicates, perfect for identifying distinct characters
    
    3. Iterate over each character in the normalized string:
        a. For each character, add it to the set of distinct characters
    
    4. After iterating over all characters, count the number of elements in the set:
        a. This count represents the number of distinct characters in the original string
    
    5. Return the count as the result
    
    Examples:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Normalize the string to lower case
    normalized_string = string.lower()
    
    # Initialize an empty set to store distinct characters
    distinct_characters = set()
    
    # Iterate over each character in the normalized string
    for char in normalized_string:
        # Add the character to the set of distinct characters
        distinct_characters.add(char)
    
    # Count the number of elements in the set
    count = len(distinct_characters)
    
    # Return the count as the result
    return count