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
    1. Define a string of vowels (both lowercase and uppercase).
    2. Create a mapping of vowels to their replacements (2 positions ahead in the alphabet).
    3. Swap the case of all letters in the input message (convert uppercase to lowercase and vice versa).
    4. Iterate through each character in the message:
       a. Check if the character is a vowel.
       b. If it's a vowel, replace it with its corresponding mapped value.
       c. If not a vowel, keep the character as is.
    5. Combine the resulting characters into the final encoded message and return it.
    """
    vowels = "aeiouAEIOU"
    vowel_map = {vowel: chr((ord(vowel) - ord('a') + 2) % 26 + ord('a')) for vowel in vowels}
    vowel_map.update({vowel.upper(): vowel_map[vowel.lower()].upper() for vowel in vowels})

    encoded_message = ""
    for char in message:
        if char in vowels:
            encoded_message += vowel_map[char]
        else:
            encoded_message += char.swapcase()

    return encoded_message