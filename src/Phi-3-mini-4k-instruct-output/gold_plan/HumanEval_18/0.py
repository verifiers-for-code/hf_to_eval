def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlapping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # Step 1: Initialize a counter variable to keep track of the number of occurrences.
    count = 0

    # Step 2: Determine the range for iteration.
    # The upper bound should be the length of the string minus the length of the substring, plus 1.
    # This ensures we don't go out of bounds and check all possible positions.
    for i in range(len(string) - len(substring) + 1):
        # Step 3: Iterate through the main string using the range determined in step 2.
        # a. For each position, extract a slice of the main string with the same length as the substring.
        slice = string[i:i+len(substring)]
        # b. Compare this slice with the substring.
        # c. If they match, increment the counter.
        if slice == substring:
            count += 1

    # Step 4: After the iteration is complete, return the final count.
    return count