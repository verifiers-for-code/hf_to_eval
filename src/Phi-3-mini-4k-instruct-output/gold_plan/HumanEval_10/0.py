def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome."""
    return s == s[::-1]

def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string."""
    if not string:
        return ''

    beginning_of_suffix = 0

    while beginning_of_suffix < len(string):
        if is_palindrome(string[beginning_of_suffix:]):
            break
        beginning_of_suffix += 1

    return string + string[:beginning_of_suffix][::-1]