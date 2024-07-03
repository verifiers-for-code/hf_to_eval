def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    result = ""
    
    for char in s:
        # Convert the character to its ASCII value using ord()
        ascii_val = ord(char)
        
        # Subtract 5 from the ASCII value to shift it back
        ascii_val -= 5
        
        # Subtract the ASCII value of 'a' to get a number between 0 and 25
        num = ascii_val - ord('a')
        
        # Use modulo 26 to handle wrap-around cases (e.g., 'a' -> 'v')
        num = num % 26
        
        # Add the ASCII value of 'a' to get back to the correct ASCII range
        ascii_val = num + ord('a')
        
        # Convert the resulting ASCII value back to a character using chr()
        decoded_char = chr(ascii_val)
        
        # Append the decoded character to the result string
        result += decoded_char
    
    return result