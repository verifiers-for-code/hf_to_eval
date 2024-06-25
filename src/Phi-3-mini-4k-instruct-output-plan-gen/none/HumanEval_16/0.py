
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case
    string = string.lower()

    # Create a set to store distinct characters
    distinct_chars = set()

    # Iterate through the string and add each character to the set
    for char in string:
        distinct_chars.add(char)

    # Return the number of distinct characters
    return len(distinct_chars)