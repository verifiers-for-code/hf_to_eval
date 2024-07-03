def reverse_delete(s, c):
    """
    Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    
    1. Create a dictionary to store characters and their frequencies in the second string:
       - Initialize an empty dictionary
       - Iterate through each character in the second string
       - For each character, increment its count in the dictionary (or set it to 1 if it's the first occurrence)
    
    2. Iterate through the first string and delete characters that match those in the second string:
       - Initialize an empty string to store the result
       - Iterate through each character in the first string
       - Check if the character is in the dictionary and its count is greater than 0
       - If the character matches, decrement its count in the dictionary
       - If the count becomes 0, remove the character from the dictionary
       - Otherwise, add the character to the result string
    
    3. Reverse the resulting string:
       - Use slicing or a suitable method to reverse the result string
    
    4. Check if the original and reversed strings are equal:
       - Compare the original result string with its reversed version
       - If they are equal, the string is a palindrome
    
    5. Return the result string and a boolean indicating if it's a palindrome:
       - Return a tuple containing the result string and a boolean value (True or False)
    
    Additional implementation details:
    - Use a dictionary to efficiently store and look up character frequencies
    - Use string concatenation or a list to build the result string
    - Consider using a conditional expression or a boolean variable to indicate if the string is a palindrome
    - Ensure that the function handles empty input strings and characters correctly
    """
    char_freq = {}
    for char in c:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    result = ""
    for char in s:
        if char in char_freq and char_freq[char] > 0:
            char_freq[char] -= 1
        else:
            result += char
    
    reversed_result = result[::-1]
    is_palindrome = result == reversed_result
    
    return (result, is_palindrome)