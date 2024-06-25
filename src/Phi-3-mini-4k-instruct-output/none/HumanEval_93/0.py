def encode(message):
    """
    Write a function that takes a message, and encodes in such a way that it swaps case of all letters,
    replaces all vowels in the message with the letter that appears 2 places ahead of that vowel in the English alphabet.
    
    Args:
    message (str): The message to be encoded.
    
    Returns:
    str: The encoded message.
    """
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    
    for char in message:
        if char.isalpha():
            # Swap case
            if char.islower():
                encoded_message += char.upper()
            else:
                encoded_message += char.lower()
            
            # Replace vowels
            if char in vowels:
                new_char = chr(ord(char) + 2)
                if new_char > 'Z':
                    new_char = chr(ord(new_char) - 26)
                encoded_message += new_char
        else:
            encoded_message += char
            
    return encoded_message