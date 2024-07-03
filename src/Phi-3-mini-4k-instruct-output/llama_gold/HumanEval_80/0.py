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
    1. Check if the length of the input string is less than 3. If so, return False immediately, as it cannot be a happy string.
    2. Initialize a loop that iterates through the string, considering 3 consecutive characters at a time (a sliding window).
    3. Within the loop, check if any of the 3 characters are the same (using equality checks).
       a. If any of the characters are equal, return False, as the string is not happy.
    4. If the loop completes without finding any equal characters, return True, indicating the string is happy."""
    
    if len(s) < 3:
        return False
    
    for i in range(len(s) - 2):
        if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
            return False
    
    return True