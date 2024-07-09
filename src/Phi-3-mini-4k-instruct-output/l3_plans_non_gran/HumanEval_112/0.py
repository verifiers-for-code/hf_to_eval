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
    1. Initialize an empty string to store the filtered characters from s.
    2. Iterate through each character in s:
        a. Check if the character is not present in c.
        b. If the character is not present, add it to the filtered string.
    3. After filtering, check if the filtered string is equal to its reverse.
    4. If the filtered string is equal to its reverse, set a flag to True (indicating it's a palindrome).
    5. Return a tuple containing the filtered string and the palindrome flag."""
    
    filtered_string = ""
    for char in s:
        if char not in c:
            filtered_string += char
    
    is_palindrome = filtered_string == filtered_string[::-1]
    
    return (filtered_string, is_palindrome)