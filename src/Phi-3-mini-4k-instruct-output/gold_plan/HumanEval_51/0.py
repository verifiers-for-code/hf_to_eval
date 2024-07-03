def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Action Plan:
    1. Initialize an empty result string to store non-vowel characters.
    2. Create a list or set of vowels (both lowercase and uppercase) for easy checking.
    3. Iterate through each character in the input 'text':
       a. Convert the character to lowercase for case-insensitive comparison.
       b. Check if the lowercase character is not in the vowels list/set.
       c. If it's not a vowel, add the original character to the result string.
    4. Return the result string containing only non-vowel characters.

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
    vowels = set('aeiouAEIOU')
    result = ''
    for char in text:
        if char not in vowels:
            result += char
    return result