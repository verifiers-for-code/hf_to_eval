
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
    """
    # Remove spaces and convert to lowercase
    text = text.replace(' ', '').lower()

    # Check if the string is equal to its reverse
    return text == text[::-1]