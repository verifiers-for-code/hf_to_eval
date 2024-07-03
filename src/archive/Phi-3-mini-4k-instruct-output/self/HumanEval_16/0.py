def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Step 1: Normalize the string to ensure case-insensitivity
    normalized_string = string.lower()
    
    # Step 2: Initialize an empty set to store distinct characters
    distinct_characters = set()
    
    # Step 3: Iterate over each character in the normalized string
    for char in normalized_string:
        # Add each character to the set of distinct characters
        distinct_characters.add(char)
    
    # Step 4: Count the number of elements in the set
    num_distinct_characters = len(distinct_characters)
    
    # Step 5: Return the count as the result
    return num_distinct_characters