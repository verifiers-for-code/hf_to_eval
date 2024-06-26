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
    # Handle the edge case: an empty string is considered a palindrome
    if text == '':
        return True

    # Set up a loop to iterate through half of the string
    for i in range(len(text) // 2):
        # Compare the character at index i with the character at the corresponding index from the end
        if text[i] != text[len(text) - 1 - i]:
            # If they don't match, return False immediately
            return False

    # If the loop completes without returning False, return True
    return True