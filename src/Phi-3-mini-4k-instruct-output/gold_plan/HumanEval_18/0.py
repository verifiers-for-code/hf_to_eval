def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3

    Action Plan:
    1. Initialize a counter variable to keep track of the number of occurrences.
    2. Determine the range for iteration:
       - The upper bound should be the length of the string minus the length of the substring, plus 1.
       This ensures we don't go out of bounds and check all possible positions.
    3. Iterate through the main string using the range determined in step 2:
       a. For each position, extract a slice of the main string with the same length as the substring.
       b. Compare this slice with the substring.
       c. If they match, increment the counter.
    4. After the iteration is complete, return the final count.

    Note: This approach allows for counting overlapping occurrences.
    """
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count