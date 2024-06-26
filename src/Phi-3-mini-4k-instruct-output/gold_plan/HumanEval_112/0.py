def reverse_delete(s, c):
    """Task
    We are given two strings s and c, you have to delete all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    
    Action Plan:
    1. Create a new string by removing characters:
       a. Iterate through each character in s
       b. If the character is not in c, add it to the new string
    
    2. Check if the new string is a palindrome:
       a. Compare the new string with its reverse
    
    3. Return the result:
       a. Create a tuple with the new string and the palindrome check result
       b. Return the tuple
    """
    # Step 1: Create a new string by removing characters
    new_s = ''.join([char for char in s if char not in c])
    
    # Step 2: Check if the new string is a palindrome
    is_palindrome = new_s == new_s[::-1]
    
    # Step 3: Return the result
    return (new_s, is_palindrome)