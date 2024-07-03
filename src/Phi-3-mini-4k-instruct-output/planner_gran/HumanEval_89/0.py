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
    

    1. Define the alphabet:
       - Create a string variable to store the alphabet (e.g., 'abcdefghijklmnopqrstuvwxyz')
    
    2. Rotate the alphabet:
       - Shift each character in the alphabet down by two places (e.g., 'z' becomes 'b', 'y' becomes 'a')
       - Use string slicing to achieve this rotation
    
    3. Encrypt each character in the input string:
       - Iterate through each character in the input string
       - For each character:
         a. Check if it's an alphabetic character
         b. If it's alphabetic:
            - Find the index of the character in the rotated alphabet
            - Use this index to retrieve the corresponding character from the rotated alphabet
            - Add the encrypted character to a new string
         c. If it's not alphabetic:
            - Add the original character to the new string (no encryption needed)
    
    4. Handle non-alphabetic characters:
       - Ensure that non-alphabetic characters (e.g., spaces, punctuation) are preserved in the encrypted string
    
    5. Return the encrypted string:
       - After processing all characters, return the encrypted string
    
    Additional implementation details:
    - Use the `isalpha()` method to check if a character is alphabetic
    - Use the `index()` method to find the index of a character in the alphabet
    - Use string concatenation to build the encrypted string
    - Ensure that the function handles empty input strings correctly"""

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_alphabet = alphabet[2:] + alphabet[:2]
    encrypted_string = ''

    for char in s:
        if char.isalpha():
            index = rotated_alphabet.index(char.lower())
            encrypted_char = rotated_alphabet[index]
            encrypted_string += encrypted_char
        else:
            encrypted_string += char

    return encrypted_string