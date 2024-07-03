def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlapping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # Step 1: Handle edge cases
    if not string:
        return 0
    
    # Step 2: Pre-compute the length of the original string
    string_length = len(string)
    
    # Step 3: Loop through the original string
    count = 0
    start_index = 0
    while start_index <= string_length - len(substring):
        # Step 4: Check for the substring
        if string[start_index:start_index+len(substring)] == substring:
            count += 1
            # Step 5: Update the start index for the next search
            start_index += 1
        else:
            # If no match is found, break the loop
            break
    
    # Step 6: Return the final count
    return count