def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string, counting overlapping cases.
    
    Action Plan:
    1. Understand the problem: Find how many times a given substring can be found in the original string, counting overlapping cases.
    2. Initialize a counter variable to store the number of occurrences.
    3. Use a loop to iterate through the original string, starting from the beginning.
    4. In each iteration, check if the substring is found at the current index in the original string.
    5. If the substring is found, increment the counter and update the starting index for the next search to the end of the current occurrence.
    6. Continue the loop until the substring is no longer found in the original string.
    7. If the substring is not found, return the counter as the result.
    8. Consider handling edge cases, such as an empty original string or substring.
    """
    count = 0
    start = 0
    while True:
        start = string.find(substring, start)
        if start == -1:
            break
        count += 1
        start += 1
    return count