def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    
    Action Plan:
    1. Convert the input string to lowercase to ensure case-insensitivity.
       Hint: Use a string method that converts all characters to lowercase.
    
    2. Create a collection of unique characters from the lowercase string.
       Hint: Consider using a data structure that automatically eliminates duplicates.
    
    3. Count the number of elements in this collection of unique characters.
       Hint: Use a function or method that returns the size or length of the collection.
    
    4. Return the count as an integer.
    
    Remember: The goal is to count distinct characters regardless of case, 
    so 'a' and 'A' should be counted as the same character.
    """
    # Step 1: Convert the input string to lowercase
    lowercase_string = string.lower()
    
    # Step 2: Create a collection of unique characters
    unique_characters = set(lowercase_string)
    
    # Step 3: Count the number of elements in the collection
    count = len(unique_characters)
    
    # Step 4: Return the count
    return count