def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome 

    Test if given string is a palindrome Action Plan:
    1. Define the helper function for palindrome detection:
    2. Function implementation:
    3. Algorithm for `make_palindrome(string)`:
    4. Plan for optimizing the function:
    5. Testing:
    """
    # Helper function to check if a string is a palindrome
    def is_palindrome_helper(s: str) -> bool:
        return s == s[::-1]

    # Check if the given string is a palindrome
    return is_palindrome_helper(string)


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    # Edge case: empty string
    if not string:
        return string

    # Find the longest palindromic suffix
    for i in range(len(string), 0, -1):
        if is_palindrome(string[-i:]):
            suffix = string[-i:]
            break
    else:
        # If no palindromic suffix is found, return the original string
        return string

    # Find the prefix that comes before the palindromic suffix
    prefix = string[:-len(suffix)]

    # Reverse the prefix and append it to the suffix
    return prefix[::-1] + suffix