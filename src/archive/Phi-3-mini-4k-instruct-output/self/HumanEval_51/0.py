def remove_vowels(text):
    """
    remove_vowels is a function that takes a string and returns a string without vowels.
    
    Args:
    text (str): The input string.
    
    Returns:
    str: The input string without vowels.
    
    Examples:
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    vowels = set("aeiouAEIOU")
    result = ""
    
    for char in text:
        if char not in vowels:
            result += char
            
    return result