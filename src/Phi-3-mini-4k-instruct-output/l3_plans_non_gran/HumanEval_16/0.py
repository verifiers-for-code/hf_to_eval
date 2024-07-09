def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    

    Action Plan:
    1. Convert the input string to lowercase to ensure case-insensitive comparison.
    2. Remove duplicate characters from the string:
        - Use a data structure (e.g., set) to store unique characters
        - Iterate through each character in the string
        - Add each character to the set (ignoring duplicates)
    3. Count the number of distinct characters:
        - Use the length of the set to get the count of unique characters
    4. Return the count of distinct characters
    
    Note: Consider using a set for efficient duplicate removal and counting.
    Be mindful of case sensitivity when converting the input string."""
    
    # Step 1: Convert the input string to lowercase
    string = string.lower()
    
    # Step 2: Remove duplicate characters using a set
    unique_characters = set(string)
    
    # Step 3: Count the number of distinct characters
    count = len(unique_characters)
    
    # Step 4: Return the count of distinct characters
    return count