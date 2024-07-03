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
    1. Initialize an empty string result to build the resulting string after deletion.
    
    2. Iterate over each character in the input string s using a loop.
    
    3. Inside the loop:
        a. Check if the character matches any character in string c.
        b. If not, append the character to result.
    
    4. After building the result string, check if it is a palindrome:
        a. Initialize a boolean variable is_palindrome to True.
        b. Use a loop to compare the first and last characters, moving towards the center.
        c. Break the loop if any pair of characters does not match.
        d. If the loop completes, is_palindrome remains True.
    
    5. Form the result tuple with the resulting string and the boolean palindrome status.
    
    6. Return the result tuple.
    
    7. Handle special cases, such as empty input strings or an empty result string (since removing all characters should result in an empty string)."""
    
    result = ""
    for char in s:
        if char not in c:
            result += char
    
    is_palindrome = True
    for i in range(len(result) // 2):
        if result[i] != result[-i - 1]:
            is_palindrome = False
            break
    
    return (result, is_palindrome)