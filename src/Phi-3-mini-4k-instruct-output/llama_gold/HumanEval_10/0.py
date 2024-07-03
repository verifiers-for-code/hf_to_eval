def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome 

    Test if given string is a palindrome Action Plan:
    1. If the input string is empty, return an empty string.
    2. Initialize a variable to track the starting index of the longest palindromic suffix.
    3. Iterate through the input string from the end:
       a. Check if the substring from the current index to the end is a palindrome.
       b. If it's not a palindrome, increment the starting index.
    4. Once the longest palindromic suffix is found, append the reversed prefix (from the start of the string to the starting index) to the original string.
    5. Return the resulting palindrome string.
    """
    if not string:
        return ""

    start = 0
    for i in range(len(string), 0, -1):
        if string[i-1] == string[len(string)-i]:
            start = i-1
        else:
            break

    return string + string[:start][::-1]


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
    return is_palindrome(string)