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
    1. Initialize an empty string to store the encoded message.
    2. Iterate through each character in the input message:
        a. Check if the character is a letter (both uppercase and lowercase).
        b. If it's a letter:
            - Swap the case of the letter (uppercase to lowercase or vice versa).
            - Check if the letter is a vowel (a, e, i, o, u).
            - If it's a vowel:
                - Find the letter that appears 2 places ahead in the alphabet.
                - Append this letter to the encoded message.
            - If it's not a vowel:
                - Append the letter to the encoded message.
        c. If the character is not a letter:
            - Append the character to the encoded message as is.
    3. Return the final encoded message.
    
    Note: Use appropriate string methods for case swapping and character checking.
    Be careful when handling the vowel replacement and non-letter characters.
    """
    encoded_message = ""
    vowels = "aeiouAEIOU"
    for char in message:
        if char.isalpha():
            # Swap case
            encoded_char = char.swapcase()
            # Check if it's a vowel
            if encoded_char in vowels:
                # Find the letter that appears 2 places ahead
                if encoded_char == 'A':
                    encoded_char = 'C'
                elif encoded_char == 'E':
                    encoded_char = 'G'
                elif encoded_char == 'I':
                    encoded_char = 'K'
                elif encoded_char == 'O':
                    encoded_char = 'Q'
                elif encoded_char == 'U':
                    encoded_char = 'W'
                encoded_message += encoded_char
            else:
                encoded_message += encoded_char
        else:
            encoded_message += char
    return encoded_message