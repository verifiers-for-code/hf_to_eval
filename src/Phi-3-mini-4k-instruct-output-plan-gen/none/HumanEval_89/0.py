
def encrypt(s):
    # Define the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Create a rotated alphabet
    rotated_alphabet = alphabet[2:] + alphabet[:2]

    # Create a translation table
    translation_table = str.maketrans(alphabet, rotated_alphabet)

    # Encrypt the string
    encrypted_string = s.translate(translation_table)

    return encrypted_string