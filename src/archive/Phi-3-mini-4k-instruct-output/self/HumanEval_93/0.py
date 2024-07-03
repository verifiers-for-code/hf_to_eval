def swap_case(char):
    """
    Swaps the case of a single character:
    - If the character is an uppercase letter, convert it to lowercase
    - Otherwise, convert it to uppercase
    """
    if char.isupper():
        return char.lower()
    else:
        return char.upper()

def encode(message):
    """
    Encodes a message by swapping the case of all letters and replacing all vowels
    with the letter that appears two places ahead in the English alphabet.
    """
    vowel_map = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w'}
    encoded_message = []

    for char in message:
        if char.lower() in vowel_map:
            encoded_message.append(vowel_map[char.lower()])
        else:
            encoded_message.append(swap_case(char))

    return ''.join(encoded_message)