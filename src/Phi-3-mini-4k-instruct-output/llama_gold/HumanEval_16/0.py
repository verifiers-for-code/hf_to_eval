def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    

    Action Plan:
    1. Convert the input string to a uniform case (e.g., lowercase) to ignore case differences.
    2. Remove duplicates from the string to get a collection of unique characters.
    3. Count the number of elements in the collection of unique characters.
    4. Return the count as the result.
    
    Note: Consider using a data structure that automatically removes duplicates, such as a set, to make the implementation more efficient."""
    
    # Step 1: Convert the input string to lowercase
    string = string.lower()
    
    # Step 2: Remove duplicates by converting the string to a set
    unique_characters = set(string)
    
    # Step 3: Count the number of elements in the set
    count = len(unique_characters)
    
    # Step 4: Return the count
    return count