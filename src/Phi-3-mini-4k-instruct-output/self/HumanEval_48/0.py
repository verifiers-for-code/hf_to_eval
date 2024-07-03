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
    1. Normalize the input:
        a. Convert the text to lowercase
        b. Remove non-alphanumeric characters
    
    2. Create a loop to compare characters:
        a. Set two pointers, one at the start and one at the end
        b. Move the start pointer forward and the end pointer backward
        c. Compare characters at the pointers
        d. Stop the loop when the pointers meet or cross each other
    
    3. Determine if the input is a palindrome:
        a. If the loop completes without finding a mismatch, the input is a palindrome
        b. Otherwise, it is not
    
    4. Consider edge cases:
        a. An empty string is technically a palindrome
        b. A string with no alphanumeric characters can be considered a palindrome
        c. A single-character string is a palindrome
    
    5. Return the result:
        a. Return True if the input is a palindrome
        b. Return False otherwise"""
    
    # Normalize the input
    text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Create a loop to compare characters
    start, end = 0, len(text) - 1
    while start < end:
        if text[start] != text[end]:
            return False
        start += 1
        end -= 1
    
    # Determine if the input is a palindrome
    return True