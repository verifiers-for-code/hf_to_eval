def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Step 1: Convert the input string to lowercase
    lowercase_string = string.lower()

    # Step 2: Create a collection of unique characters from the lowercase string
    unique_chars = set(lowercase_string)

    # Step 3: Count the number of elements in this collection of unique characters
    count = len(unique_chars)

    # Step 4: Return the count as an integer
    return count