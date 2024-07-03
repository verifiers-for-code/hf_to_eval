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
    
    1. Check the length of the input string:
       - Use the built-in len() function to get the length of the string
       - If the length is less than 3, immediately return False (not a happy string)
    
    2. Initialize a flag or variable to track if the string is happy:
       - Set a boolean variable (e.g., happy) to True initially
    
    3. Iterate through the string, checking for distinct 3 consecutive characters:
       - Use a loop to iterate through the string, considering each character and its next two characters
       - For each iteration, check if the current character is the same as the next two characters
       - If a match is found, set the happy flag to False and break the loop
    
    4. Return the result:
       - If the happy flag is still True after the loop, return True (the string is happy)
       - If the happy flag is False, return False (the string is not happy)
    
    Additional implementation details:
    - Use a loop to iterate through the string, considering each character and its next two characters
    - Use conditional statements to check for distinct 3 consecutive characters
    - Use a boolean variable to track the happiness of the string
    - Return the result based on the value of the happy variable"""
    if len(s) < 3:
        return False
    happy = True
    for i in range(len(s)-2):
        if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:
            happy = False
            break
    return happy