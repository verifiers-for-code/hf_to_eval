def encrypt(s):
    # Step 1: Create a string variable containing the lowercase alphabet in order.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # Step 2: Initialize an empty string to store the encrypted result.
    encrypted_result = ''
    
    # Step 3: Iterate through each character in the input string 's'.
    for char in s:
        # Check if the character is in the alphabet.
        if char in alphabet:
            # Find its index in the alphabet.
            index = alphabet.index(char)
            
            # Calculate the new index by adding 4 (2*2) to the current index.
            new_index = (index + 4) % 26
            
            # Get the character at the new index in the alphabet.
            encrypted_char = alphabet[new_index]
            
            # Append the resulting character to the output string.
            encrypted_result += encrypted_char
        else:
            # If the character is not in the alphabet, keep it unchanged.
            encrypted_result += char
    
    # Step 4: Return the final encrypted string.
    return encrypted_result