def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome 

     Test if given string is a palindrome Action Plan:
     Test if given string is a palindrome 1. Define the make_palindrome function with a string parameter.
     Test if given string is a palindrome 2. Initialize an empty string to store the result.
     Test if given string is a palindrome 3. Check if the input string is already a palindrome using the is_palindrome function.
     Test if given string is a palindrome 4. If the string is a palindrome, return it as is.
     Test if given string is a palindrome 5. If the string is not a palindrome:
     Test if given string is a palindrome     a. Find the longest postfix of the string that is a palindrome using the is_palindrome function.
     Test if given string is a palindrome     b. Extract the prefix of the string before the palindromic suffix.
     Test if given string is a palindrome     c. Append the reverse of the prefix to the end of the string.
     Test if given string is a palindrome     d. Return the resulting palindrome.
     Test if given string is a palindrome 6. Consider edge cases, such as an empty input string, and handle them appropriately.
     Test if given string is a palindrome 7. Test the function with various input strings to ensure it works correctly."""
    return string == string[::-1]


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
    if is_palindrome(string):
        return string

    for i in range(len(string), 0, -1):
        if is_palindrome(string[:i]):
            prefix = string[:i]
            suffix = string[i:]
            return prefix + suffix[::-1]

    return string