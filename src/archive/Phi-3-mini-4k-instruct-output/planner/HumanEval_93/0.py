def encode(message):
    """
    Encode a message by swapping the case of all letters and replacing all vowels with the letter that appears 2 places ahead in the English alphabet.
    
    Args:
    message (str): The input message to be encoded.
    
    Returns:
    str: The encoded message.
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    encoded_message = ""
    vowels = "aeiouAEIOU"
    vowel_mapping = {
        "a": "c",
        "e": "g",
        "i": "k",
        "o": "q",
        "u": "w",
        "A": "C",
        "E": "G",
        "I": "K",
        "O": "Q",
        "U": "W"
    }

    for char in message:
        if char.isalpha():
            # Swap case
            encoded_char = char.swapcase()
            # Check if the character is a vowel
            if encoded_char in vowels:
                # Replace vowel with the letter 2 places ahead
                encoded_char = vowel_mapping[encoded_char]
        else:
            encoded_char = char

        encoded_message += encoded_char

    return encoded_message