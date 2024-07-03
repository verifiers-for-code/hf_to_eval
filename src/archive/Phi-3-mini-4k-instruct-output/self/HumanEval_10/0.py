def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""
    
    # Find the longest palindromic suffix
    for i in range(len(string), 0, -1):
        suffix = string[i-1:]
        if is_palindrome(suffix):
            break
    
    # Extract the prefix and reverse it
    prefix = string[:len(string)-i+1]
    reversed_prefix = prefix[::-1]
    
    # Append the reversed prefix to the suffix
    return reversed_prefix + string