def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    

    Action Plan:
    1. Define a dictionary or list to map each vowel to its "two places ahead" counterpart in the alphabet (e.g., a->c, e->g).
    
    2. Define a function to swap the case of a single character:
        a. Check if the character is an uppercase letter; if so, convert it to lowercase
        b. Otherwise, convert it to uppercase
    
    3. Create the main encode function with the following steps:
        a. Initialize an empty list to store the encoded message
        b. Iterate over each character in the message:
            i. If the character is a vowel, replace it with its mapped value
            ii. Otherwise, apply the case swap function
            iii. Append the transformed character to the encoded message list
    
    4. Join the list into a single string and return it
    
    5. Handle edge cases such as the last character of the message, ensuring proper sequence and character handling.
    """
    # Step 1: Define a dictionary to map each vowel to its "two places ahead" counterpart in the alphabet
    vowel_map = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w'}
    
    # Step 2: Define a function to swap the case of a single character
    def swap_case(char):
        if char.isupper():
            return char.lower()
        else:
            return char.upper()
    
    # Step 3: Create the main encode function
    encoded_message = []
    for char in message:
        # Check if the character is a vowel
        if char in vowel_map:
            # Replace it with its mapped value
            encoded_message.append(vowel_map[char])
        else:
            # Apply the case swap function
            encoded_message.append(swap_case(char))
    
    # Step 4: Join the list into a single string and return it
    return ''.join(encoded_message)