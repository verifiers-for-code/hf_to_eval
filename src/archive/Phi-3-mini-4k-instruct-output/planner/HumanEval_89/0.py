def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    
    Action Plan:
    1. Define the original alphabet and the rotated alphabet.
    2. Create a dictionary to map each character in the original alphabet to its corresponding character in the rotated alphabet.
    3. Define the encryption function `encrypt` that takes a string `s` as input.
    4. Initialize an empty string `encrypted` to store the encrypted result.
    5. Iterate through each character `c` in the input string `s`:
        a. Check if `c` is an alphabetic character.
        b. If `c` is alphabetic, find its corresponding character in the rotated alphabet using the mapping dictionary.
        c. If `c` is not alphabetic, leave it unchanged.
        d. Append the encrypted character to the `encrypted` string.
    6. Return the `encrypted` string.
    7. Consider handling edge cases, such as empty input strings or non-alphabetic characters.
    """
    original_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_alphabet = 'cdefghijklmnopqrstuvwxyzab'
    mapping = {original_alphabet[i]: rotated_alphabet[i] for i in range(len(original_alphabet))}

    encrypted = ''
    for c in s:
        if c.isalpha():
            encrypted += mapping[c]
        else:
            encrypted += c

    return encrypted