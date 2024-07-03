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
    
    def rotate_letter(letter):
        """Helper function to rotate a single letter.
        Shifts the letter using ASCII values, adjusts for wrap-around,
        and ensures proper handling of both uppercase and lowercase letters.
        """
        if not letter.isalpha():
            return letter
        
        ascii_offset = 65 if letter.isupper() else 97
        rotated_ascii = (ord(letter) - ascii_offset + 2) % 26 + ascii_offset
        return chr(rotated_ascii)
    
    encrypted_string = ''.join(rotate_letter(char) for char in s)
    return encrypted_string