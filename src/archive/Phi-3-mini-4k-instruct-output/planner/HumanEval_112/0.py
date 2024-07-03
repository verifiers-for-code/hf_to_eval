def reverse_delete(s, c):
    """
    Task: Given two strings s and c, delete all characters in s that are equal to any character in c,
    then check if the result string is a palindrome.

    Parameters:
    s (str): The input string.
    c (str): The string containing characters to be deleted from s.

    Returns:
    tuple: A tuple containing the result string and a boolean value indicating whether it's a palindrome.

    Example:
    >>> reverse_delete("abcde", "ae")
    ('bcd', False)
    >>> reverse_delete("abcdef", "b")
    ('acdef', False)
    >>> reverse_delete("abcdedcba", "ab")
    ('cdedc', True)
    """
    result = ''.join([char for char in s if char not in c])
    is_palindrome = result == result[::-1]
    return (result, is_palindrome)