def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string, counting overlapping cases.

    Args:
    string (str): The original string to search in.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring is found in the original string, counting overlapping cases.

    Examples:
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    2
    """
    # Initialize a counter variable to store the number of occurrences
    count = 0

    # Use a loop to iterate through the original string, starting from the beginning
    start_index = 0
    while start_index < len(string):
        # Check if the substring is found at the current index in the original string
        if string[start_index:start_index+len(substring)] == substring:
            # Increment the counter and update the starting index for the next search to the end of the current occurrence
            count += 1
            start_index += len(substring)
        else:
            # If the substring is not found, break the loop
            break

    # Return the counter as the result
    return count