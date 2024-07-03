def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    

    Action Plan:
    1. Initialize a counter to store the number of times the substring appears in the string.
    2. Iterate through the input string, considering each position as a potential starting point for the substring:
       a. Check if the substring matches the characters in the string starting from the current position.
       b. If a match is found, increment the counter.
    3. Continue iterating through the string, checking for matches at each position.
    4. Return the final count of how many times the substring appears in the string."""
    
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count