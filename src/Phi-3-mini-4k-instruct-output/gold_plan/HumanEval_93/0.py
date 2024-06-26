def encode(message):
    # Step 1: Define a string containing all vowels (both lowercase and uppercase)
    vowels = 'aeiouAEIOU'
    
    # Step 2: Create a dictionary to map vowels to their replacements
    vowel_replacements = {vowel: chr((ord(vowel.lower()) - 97 + 2) % 26 + 97) for vowel in vowels}
    
    # Step 3: Swap the case of the entire input message
    swapped_message = message.swapcase()
    
    # Step 4: Iterate through each character in the case-swapped message
    encoded_message = ''.join([
        vowel_replacements.get(char, char) if char in vowels else char
        for char in swapped_message
    ])
    
    # Step 5: Join the transformed characters into a single string
    # (Already done in Step 4)
    
    # Step 6: Return the encoded message
    return encoded_message