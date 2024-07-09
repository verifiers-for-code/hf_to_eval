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
    1. Define the function `is_palindrome` with a string parameter `text`.
    2. Handle the edge case where the input string is empty (`text == ''`):
        - Return `True` immediately, as an empty string is considered a palindrome.
    3. Reverse the input string `text` using slicing or other methods.
    4. Compare the original string `text` with the reversed string:
        - If they are equal, return `True`, indicating that the string is a palindrome.
        - If they are not equal, return `False`, indicating that the string is not a palindrome.
    5. Ensure the function returns a boolean value (`True` or `False`).
    
    Note: Consider using Python's built-in slicing feature to reverse the string efficiently.
    Be mindful of the function's docstring and ensure it accurately describes the implementation.
    """
    if text == '':
        return True
    return text == text[::-1]