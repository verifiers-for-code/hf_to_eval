def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    

    Action Plan:
    1. Initialize a variable to track the result (assuming the string is a palindrome).
    2. Iterate through the input string, considering each character and its corresponding character from the end:
       a. Compare the current character with the character at the mirrored position (from the end).
       b. If the characters don't match, immediately return False (the string is not a palindrome).
    3. If the loop completes without finding any mismatch, return True (the string is a palindrome).
    """
    result = True
    for i in range(len(text) // 2):
        if text[i] != text[-i - 1]:
            result = False
            break
    return result