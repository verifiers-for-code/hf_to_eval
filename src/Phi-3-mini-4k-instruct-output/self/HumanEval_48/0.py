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
    # Normalize the input
    text = text.lower()
    text = ''.join(char for char in text if char.isalnum())

    # Create a loop to compare characters
    start, end = 0, len(text) - 1
    while start < end:
        if text[start] != text[end]:
            return False
        start += 1
        end -= 1

    # Determine if the input is a palindrome
    return True