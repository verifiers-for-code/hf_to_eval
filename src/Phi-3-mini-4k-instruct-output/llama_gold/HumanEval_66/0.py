def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only's ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    

    Action Plan:
    1. Check if the input string is empty. If so, return 0 immediately.
    2. Initialize a variable to store the sum of ASCII codes.
    3. Iterate through each character in the input string:
       a. Check if the character is uppercase using a string method.
       b. If the character is uppercase, calculate its ASCII code using a built-in function.
       c. Add the ASCII code to the sum variable.
    4. After iterating through all characters, return the sum of ASCII codes."""
    
    if not s:
        return 0
    
    ascii_sum = 0
    for char in s:
        if char.isupper():
            ascii_sum += ord(char)
    
    return ascii_sum