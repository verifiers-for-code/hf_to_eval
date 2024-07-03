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
    # Step 1: Handle the edge case: an empty string is considered a palindrome
    if text == '':
        return True

    # Step 2: Set up a loop to iterate through half of the string
    for i in range(len(text) // 2):
        # Step 3a: Compare the character at index i with the character at the opposite end
        if text[i] != text[len(text) - 1 - i]:
            # Step 3b: If they don't match, return False immediately
            return False

    # Step 4: If the loop completes without returning False, return True
    return True