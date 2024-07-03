def swap_case(char):
    """
    Swap the case of a single character.
    """
    if char.isupper():
        return char.lower()
    else:
        return char.upper()

def encode(message):
    """
    Encode a message by swapping the case of all letters and replacing vowels with the letter that appears 2 places ahead in the alphabet.
    """
    # Step 1: Define a dictionary to map each vowel to its "two places ahead" counterpart in the alphabet
    vowel_map = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w'}

    # Step 2: Initialize an empty list to store the encoded message
    encoded_message = []

    # Step 3: Iterate over each character in the message
    for char in message:
        # Check if the character is a vowel
        if char.lower() in vowel_map:
            # Replace it with its mapped value
            encoded_char = vowel_map[char.lower()]
        else:
            # Apply the case swap function
            encoded_char = swap_case(char)

        # Append the transformed character to the encoded message list
        encoded_message.append(encoded_char)

    # Step 4: Join the list into a single string and return it
    return ''.join(encoded_message)