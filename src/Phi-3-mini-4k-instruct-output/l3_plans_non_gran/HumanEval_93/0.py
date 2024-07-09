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
    1. Define a function `encode` that takes a string `message` as input.
    2. Initialize an empty string `encoded_message` to store the encoded message.
    3. Iterate through each character `char` in the `message`:
        a. Check if `char` is a letter using the `isalpha()` method.
        b. If `char` is a letter:
            - Check if it's a vowel (a, e, i, o, u) using a conditional statement.
            - If it's a vowel:
                - Calculate the letter 2 places ahead in the alphabet using the `ord()` function.
                - Convert the calculated letter back to a character using the `chr()` function.
                - Append the replaced letter to `encoded_message`.
            - If it's not a vowel:
                - Swap the case of `char` using the `swapcase()` method.
                - Append the swapped character to `encoded_message`.
        c. If `char` is not a letter, append it to `encoded_message` as is.
    4. Return the `encoded_message` string.
    """
    encoded_message = ""
    for char in message:
        if char.isalpha():
            if char.lower() in "aeiou":
                encoded_char = chr(ord(char) + 2)
                if encoded_char > "z":
                    encoded_char = chr(ord(encoded_char) - 26)
            else:
                encoded_char = char.swapcase()
        else:
            encoded_char = char
        encoded_message += encoded_char
    return encoded_message