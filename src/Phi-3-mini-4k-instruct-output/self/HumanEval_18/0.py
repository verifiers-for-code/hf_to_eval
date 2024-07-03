def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. Count overlaping cases.
    
    Action Plan:
    1. Start with edge cases:
        - If the original string is empty, return 0
    
    2. Loop through the original string:
        - Use a start index to track where in the string to begin searching
        - Ensure the start index moves appropriately for an overlap
    
    3. Within the loop, check for the substring:
        - Compare the current slice of the string with the substring
        - If a match is found, increment the count and update the start index for the next search
    
    4. Return the final count after completing the search loop
    
    5. Consider optimization techniques:
        - Pre-compute the length of the original string to reduce the overhead of slicing inside the loop
    
    6. Additional edge case considerations:
        - Handle cases with a substring longer than the original string (should return 0)
        - Consider Unicode characters (if applicable)"""
    
    # Edge case: original string is empty
    if not string:
        return 0
    
    # Edge case: substring is longer than the original string
    if len(substring) > len(string):
        return 0
    
    count = 0
    start_index = 0
    
    # Pre-compute the length of the original string
    string_length = len(string)
    
    # Loop through the original string
    while start_index <= string_length - len(substring):
        # Check for the substring
        if string[start_index:start_index + len(substring)] == substring:
            count += 1
            start_index += 1  # Move start index for the next search
        else:
            start_index += 1  # Move start index for the next search
    
    return count