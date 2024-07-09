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
    1. Define a string of vowels (both lowercase and uppercase) to be removed from the input string.
    2. Initialize an empty string to store the result.
    3. Iterate through each character in the input string:
        a. Check if the character is not a vowel (using the defined vowels string and case-insensitive comparison).
        b. If the character is not a vowel, add it to the result string.
    4. After iterating through all characters, return the result string.
    5. Consider using a more efficient approach, such as using the `str.isalpha()` and `str.lower()` methods, to check for vowels.
    
    Note: Be careful to handle uppercase and lowercase vowels correctly.
    """
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char.lower() not in vowels:
            result += char
    return result