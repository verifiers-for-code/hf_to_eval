def is_happy(s):
    """
    You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.
    
    Parameters:
    s (str): The input string to be checked.
    
    Returns:
    bool: True if the string is happy, False otherwise.
    
    Action Plan:
    1. Define the function `is_happy` with a string `s` as input.
    2. Check if the length of the string `s` is less than 3:
        - If true, return `False` immediately, as the string is not happy.
    3. Iterate through the string `s` in chunks of 3 characters:
        - Use a loop to process each chunk of 3 characters.
        - For each chunk, check if all characters are distinct:
            a. Convert the chunk to a set to remove duplicates.
            b. Compare the length of the set with the length of the chunk.
            c. If the lengths are not equal, return `False`, as the chunk is not happy.
    4. If the loop completes without returning `False`, return `True`, indicating the string is happy.
    5. Consider adding a docstring to explain the function's purpose, parameters, and return value.
    """
    if len(s) < 3:
        return False
    
    for i in range(0, len(s) - 2, 3):
        chunk = s[i:i+3]
        if len(set(chunk)) != len(chunk):
            return False
    
    return True