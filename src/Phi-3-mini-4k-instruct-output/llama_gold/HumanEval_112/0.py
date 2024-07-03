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
    1. Initialize an empty result string to store the characters from `s` that are not in `c`.
    2. Iterate through each character in the input string `s`:
       a. Check if the character is not present in string `c`.
       b. If it's not present, add the character to the result string.
    3. Create a reverse of the result string.
    4. Check if the result string is equal to its reverse.
    5. Return a tuple containing the result string and a boolean indicating whether the string is a palindrome (True if it is, False otherwise)."""

    result = ""
    for char in s:
        if char not in c:
            result += char

    is_palindrome = result == result[::-1]

    return (result, is_palindrome)