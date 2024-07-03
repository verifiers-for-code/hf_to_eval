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

    Action Plan:
    1. Create a string variable containing the lowercase alphabet in order.
    2. Initialize an empty string to store the encrypted result.
    3. Iterate through each character in the input string 's':
       a. If the character is in the alphabet:
          i. Find its index in the alphabet.
          ii. Calculate the new index by adding 4 (2*2) to the current index.
          iii. Use modulo 26 to wrap around if the new index exceeds 25.
          iv. Get the character at the new index in the alphabet.
       b. If the character is not in the alphabet, keep it unchanged.
       c. Append the resulting character to the output string.
    4. Return the final encrypted string.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_string = ''
    for char in s:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + 4) % 26
            encrypted_string += alphabet[new_index]
        else:
            encrypted_string += char
    return encrypted_string