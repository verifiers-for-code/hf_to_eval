def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome 

     Test if given string is a palindrome Action Plan:
     Test if given string is a palindrome 1. Define a function `is_palindrome` to check if a given string is a palindrome.
     Test if given string is a palindrome 2. Implement the `is_palindrome` function using string slicing to reverse the string and compare it with the original string.
     Test if given string is a palindrome 3. Define a function `make_palindrome` to find the shortest palindrome that begins with a supplied string.
     Test if given string is a palindrome 4. Inside `make_palindrome`:
     Test if given string is a palindrome     a. Initialize a variable `suffix` to store the longest palindromic suffix.
     Test if given string is a palindrome     b. Iterate from the end of the string to the beginning:
     Test if given string is a palindrome         - Check if the current substring is a palindrome using the `is_palindrome` function.
     Test if given string is a palindrome         - If it is, update `suffix` with the current substring.
     Test if given string is a palindrome     c. Calculate the length of the `suffix`.
     Test if given string is a palindrome     d. Construct the shortest palindrome by appending the reverse of the substring before the `suffix` to the original string.
     Test if given string is a palindrome 5. Return the constructed shortest palindrome.
     Test if given string is a palindrome 6. Handle edge cases, such as an empty input string, by returning an empty string.
     Test if given string is a palindrome 
     Test if given string is a palindrome Note: Use string slicing and concatenation to manipulate the strings.
     Test if given string is a palindrome Be careful when iterating through the string to find the longest palindromic suffix."""
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
    if not string:
        return ""

    # Find the longest palindromic suffix
    for i in range(len(string), 0, -1):
        if is_palindrome(string[-i:]):
            suffix = string[-i:]
            break

    # Construct the shortest palindrome
    prefix = string[:-len(suffix)]
    return prefix + suffix + prefix[::-1]