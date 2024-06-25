
def encode(message):
    vowels = 'aeiouAEIOU'
    encoded_message = ''

    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                # Find the position of the vowel in the alphabet
                vowel_position = ord(char.lower()) - ord('a')
                # Replace the vowel with the letter 2 places ahead
                new_char = chr(ord('a') + (vowel_position + 2) % 26)
                # Preserve the case of the original character
                if char.isupper():
                    new_char = new_char.upper()
                encoded_message += new_char
            else:
                # Swap case of the character
                if char.isupper():
                    new_char = char.lower()
                else:
                    new_char = char.upper()
                encoded_message += new_char
        else:
            encoded_message += char

    return encoded_message