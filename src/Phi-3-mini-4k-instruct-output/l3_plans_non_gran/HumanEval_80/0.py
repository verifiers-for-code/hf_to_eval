def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    

    Action Plan:
    1. Validate the input:
        - Check if the input is a string
        - Raise a TypeError if the input is not a string
    
    2. Check the length of the string:
        - If the length is less than 3, return False (not happy)
    
    3. Check if every 3 consecutive letters are distinct:
        - Iterate through the string with a sliding window of size 3
        - For each window, check if all letters are unique
        - If any window has duplicate letters, return False (not happy)
    
    4. If both checks pass, return True (happy)
        - If either check fails, return False (not happy)
    
    Note: Use appropriate string methods for length and character comparison.
    Be careful with indexing when checking consecutive letters."""
    
    # Validate the input
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Check the length of the string
    if len(s) < 3:
        return False
    
    # Check if every 3 consecutive letters are distinct
    for i in range(len(s) - 2):
        if len(set(s[i:i+3])) != 3:
            return False
    
    # If both checks pass, return True
    return True