def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
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
    

    Action Plan:
    1. Define a function `remove_vowels` that takes a string `text` as input.
    2. Create a string `vowels` containing all lowercase and uppercase vowels (a, e, i, o, u).
    3. Initialize an empty string `result` to store the characters without vowels.
    4. Iterate through each character `char` in the input `text`:
        a. Check if `char` is not in `vowels` (i.e., it's not a vowel).
        b. If `char` is not a vowel, add it to the `result` string.
    5. After iterating through all characters, return the `result` string.
    6. Consider using a more efficient approach, such as a list comprehension or a generator expression, to build the `result` string.
    
    Note: Be careful when handling uppercase and lowercase vowels."""
    vowels = "aeiouAEIOU"
    result = ''.join([char for char in text if char not in vowels])
    return result