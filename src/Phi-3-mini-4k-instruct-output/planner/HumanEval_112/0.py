def reverse_delete(s, c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    

    Action Plan:
    1. Initialize an empty string to store the result.
    2. Iterate through each character in the input string s:
        a. Check if the current character is not present in the input string c.
        b. If the character is not in c, add it to the result string.
    3. After processing all characters in s, check if the result string is a palindrome:
        a. Compare the result string with its reverse.
        b. If they are equal, the result string is a palindrome.
    4. Return a tuple containing the result string and a boolean value indicating whether it's a palindrome.
    
    Note: Use appropriate string methods for character comparison and palindrome checking.
    Be careful when iterating through the strings and performing the necessary checks."""
    
    result = ""
    for char in s:
        if char not in c:
            result += char
    
    is_palindrome = result == result[::-1]
    
    return (result, is_palindrome)