def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'

    Action Plan:
    1. Define a string containing all vowels (both lowercase and uppercase).
    2. Create a dictionary to map vowels to their replacements:
       a. For each vowel, find the character 2 places ahead in the alphabet.
       b. Use a dictionary comprehension or a loop to create this mapping.
    3. Swap the case of the entire input message.
    4. Iterate through each character in the case-swapped message:
       a. If the character is a vowel, replace it using the vowel replacement dictionary.
       b. If not a vowel, keep the character as is.
    5. Join the transformed characters into a single string.
    6. Return the encoded message.
    """
    vowels = "aeiouAEIOU"
    vowel_replacements = {vowel: chr((ord(vowel) - ord('a') + 2) % 26 + ord('a')) for vowel in vowels}
    vowel_replacements.update({vowel.upper(): vowel_replacements[vowel.lower()].upper() for vowel in vowels})

    encoded_message = ""
    for char in message:
        if char in vowels:
            encoded_message += vowel_replacements[char]
        else:
            encoded_message += char.swapcase()

    return encoded_message