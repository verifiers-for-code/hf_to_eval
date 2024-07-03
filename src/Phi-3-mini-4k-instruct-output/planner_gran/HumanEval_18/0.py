def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. Count overlaping cases.
    
    1. Initialize a counter variable to store the count of occurrences
       - Set the counter to 0 initially
    
    2. Check if the input string or substring is empty:
       - If either string is empty, return the counter value (0) immediately
       - This is because an empty substring or string cannot be found within another string
    
    3. Iterate through the input string, starting from the beginning:
       - Use a loop to iterate through each character in the string
       - For each iteration, check if the substring matches the current part of the string
       - Use the `in` operator to check for substring presence
    
    4. If the substring is found, increment the counter:
       - Increment the counter by 1 each time the substring is found
       - This is because we're counting overlapping cases
    
    5. Continue iterating through the string until the end:
       - Repeat steps 3-4 until the end of the string is reached
    
    6. Return the final count:
       - Return the value of the counter, which represents the number of occurrences of the substring
    
    Additional implementation details:
    - Use a loop to iterate through the string, and keep track of the current index
    - Use string slicing to extract the current part of the string for substring checking
    - Ensure that the function handles edge cases correctly, such as empty strings or substrings
    - Consider using a more efficient algorithm, such as the Knuth-Morris-Pratt algorithm, for larger strings
    """
    count = 0
    if not string or not substring:
        return count
    
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            count += 1
    
    return count