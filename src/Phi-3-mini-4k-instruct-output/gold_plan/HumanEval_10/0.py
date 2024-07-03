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
    
    Action Plan:
    1. Handle the empty string case:
       - Check if the input string is empty and return an empty string if true
    
    2. Initialize a variable for the beginning of the palindromic suffix:
       - Create a variable (e.g., 'beginning_of_suffix') and set it to 0
    
    3. Find the longest palindromic suffix:
       - Use a while loop to iterate until a palindrome is found
       - In each iteration:
         a. Check if the substring from 'beginning_of_suffix' to the end is a palindrome
         b. If not, increment 'beginning_of_suffix'
       - Hint: Use the is_palindrome function for checking palindromes
    
    4. Construct the final palindrome:
       - Return the original string concatenated with the reversed prefix
       - The prefix is the substring from the start to 'beginning_of_suffix'
       - Hint: Use string slicing and the reverse operation [::-1] for the prefix
    """

    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    if not string:
        return string

    beginning_of_suffix = 0
    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1

    return string + string[:beginning_of_suffix][::-1]