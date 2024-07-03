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
    """
    vowels = 'aeiou'
    encoded_message = ''
    for char in message:
        if char.lower() in vowels:
            if char.isupper():
                encoded_message += chr((ord(char) - ord('A') + 2) % 26 + ord('A'))
            else:
                encoded_message += chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
        elif char.isalpha():
            if char.isupper():
                encoded_message += char.lower()
            else:
                encoded_message += char.upper()
        else:
            encoded_message += char
    return encoded_message