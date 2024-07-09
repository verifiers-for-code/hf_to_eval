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
    1. Define a function `encrypt` that takes a string `s` as an argument.
    2. Create a custom alphabet by concatenating the lowercase and uppercase alphabets.
    3. Initialize an empty string `encrypted_string` to store the encrypted characters.
    4. Iterate through each character `char` in the input string `s`:
        a. Check if the character is an alphabet letter using the `isalpha()` method.
        b. If the character is an alphabet letter:
            - Determine its index in the custom alphabet using the `index()` method.
            - Calculate the encrypted index by shifting the original index down by 4 places.
            - Use the `ord()` function to get the ASCII value of the character.
            - Use the `chr()` function to get the character at the encrypted index.
            - Add the encrypted character to `encrypted_string`.
        c. If the character is not an alphabet letter, add it to `encrypted_string` as is.
    5. Return the `encrypted_string` after processing all characters."""
    
    # Step 2: Create a custom alphabet
    custom_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # Step 3: Initialize an empty string to store the encrypted characters
    encrypted_string = ''
    
    # Step 4: Iterate through each character in the input string
    for char in s:
        # Step 4a: Check if the character is an alphabet letter
        if char.isalpha():
            # Step 4b: Determine the index of the character in the custom alphabet
            index = custom_alphabet.index(char)
            
            # Step 4b: Calculate the encrypted index
            encrypted_index = (index + 4) % len(custom_alphabet)
            
            # Step 4b: Get the encrypted character
            encrypted_char = custom_alphabet[encrypted_index]
            
            # Step 4b: Add the encrypted character to the encrypted string
            encrypted_string += encrypted_char
        else:
            # Step 4c: Add non-alphabet characters as is
            encrypted_string += char
    
    # Step 5: Return the encrypted string
    return encrypted_string