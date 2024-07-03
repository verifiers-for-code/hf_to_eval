def encode(message):
    """
    Write a function that takes a message, and encodes in such a way that it swaps case of all letters,
    replaces all vowels in the message with the letter that appears 2 places ahead of that vowel in the English alphabet.
    Assume only letters.

    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    vowels = 'aeiouAEIOU'
    encoded_message = ''

    for char in message:
        if char.isalpha():
            if char in vowels:
                # Find the index of the vowel in the vowels string
                vowel_index = vowels.index(char)
                # Replace the vowel with the letter 2 places ahead
                encoded_char = vowels[(vowel_index + 2) % len(vowels)]
            else:
                # Swap the case of the character
                if char.islower():
                    encoded_char = char.upper()
                else:
                    encoded_char = char.lower()
        else:
            encoded_char = char

        encoded_message += encoded_char

    return encoded_message