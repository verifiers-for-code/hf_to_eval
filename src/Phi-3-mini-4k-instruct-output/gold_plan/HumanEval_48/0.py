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
    1. Handle the edge case: an empty string is considered a palindrome
    2. Set up a loop to iterate through half of the string (use range and len)
    3. In each iteration:
       a. Compare the character at index i with the character at index (len(text) - 1 - i)
       b. If they don't match, return False immediately
    4. If the loop completes without returning False, return True
    
    Note: This approach compares characters from both ends moving towards the center,
    ensuring that the string reads the same forwards and backwards.
    """
    # Handle the edge case: an empty string is considered a palindrome
    if not text:
        return True

    # Iterate through half of the string
    for i in range(len(text) // 2):
        # Compare the character at index i with the character at index (len(text) - 1 - i)
        if text[i] != text[len(text) - 1 - i]:
            # If they don't match, return False immediately
            return False

    # If the loop completes without returning False, return True
    return True