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
    

    1. Initialize an empty string to store the encoded message
       - This string will hold the encoded characters
    
    2. Iterate through each character in the input message:
       a. Check if the character is a letter (using the isalpha() method)
       b. If the character is a letter:
          - Swap the case of the letter (uppercase to lowercase or vice versa)
          - Determine the ASCII value of the swapped character (using ord())
          - Calculate the ASCII value of the letter 2 places ahead in the alphabet
          - Check if the new ASCII value is within the valid range for lowercase letters (97-122)
          - If it is, add the corresponding character to the encoded message
          - If not, add the original character to the encoded message
       c. If the character is not a letter:
          - Add the original character to the encoded message (no changes needed)
    
    3. After processing all characters, return the encoded message
    
    Additional implementation details:
    - Use the appropriate string methods for swapping case (lower() and upper())
    - Use the ord() function to get the ASCII value of a character
    - Use the chr() function to get the character corresponding to an ASCII value
    - Handle edge cases, such as empty input messages or messages with no letters
    - Consider using a more efficient approach, such as using a list comprehension or generator expression, to construct the encoded message"""
    
    encoded_message = ""
    for char in message:
        if char.isalpha():
            # Swap case of the letter
            swapped_char = char.lower() if char.isupper() else char.upper()
            # Calculate the ASCII value of the letter 2 places ahead in the alphabet
            new_ascii_val = ord(swapped_char) + 2
            # Check if the new ASCII value is within the valid range for lowercase letters
            if new_ascii_val > ord('z'):
                # If not, add the original character to the encoded message
                encoded_message += char
            else:
                # If yes, add the corresponding character to the encoded message
                encoded_message += chr(new_ascii_val)
        else:
            # If the character is not a letter, add the original character to the encoded message
            encoded_message += char
    
    return encoded_message