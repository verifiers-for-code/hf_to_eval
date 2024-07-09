def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    

    Action Plan:
    1. Initialize a variable to store the count of overlapping matches, set to 0.
    2. Iterate through the original string using a loop:
        a. For each character in the string, check if the substring can be found at that position.
        b. If the substring is found, increment the count of overlapping matches.
        c. Continue iterating through the string to find more overlapping matches.
    3. Handle edge cases:
        a. If the substring is empty, return 0.
        b. If the original string is empty, return 0.
    4. Return the final count of overlapping matches.
    5. Consider using a loop with a step size equal to the length of the substring to improve efficiency.
    
    Note: Focus on understanding the problem requirements and implementing the logic correctly.
    Be careful when handling edge cases and consider using a loop with a step size for efficiency."""
    
    if substring == '':
        return 0
    if string == '':
        return 0
    
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            count += 1
    
    return count