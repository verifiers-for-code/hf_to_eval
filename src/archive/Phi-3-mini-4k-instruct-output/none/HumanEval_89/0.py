def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    # Define the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # Create a new alphabet by rotating the original alphabet by two places
    rotated_alphabet = alphabet[2:] + alphabet[:2]
    
    # Create a translation table
    translation_table = str.maketrans(alphabet, rotated_alphabet)
    
    # Encrypt the input string
    encrypted_string = s.translate(translation_table)
    
    return encrypted_string