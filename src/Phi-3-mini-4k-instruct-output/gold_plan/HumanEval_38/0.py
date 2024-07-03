def encode_cyclic(s: str):
    """
    Encodes a string by cycling groups of 3 characters.
    """
    encoded = ""
    for i in range(0, len(s), 3):
        group = s[i:i+3]
        encoded += group[-1] + group[1] + group[0]
    return encoded

def decode_cyclic(s: str):
    """
    Takes as input a string encoded with encode_cyclic function. Returns decoded string.
    """
    # Call the encode_cyclic function on the input string 's'.
    encoded = encode_cyclic(s)
    
    # Call the encode_cyclic function again on the result of step 3.
    decoded = encode_cyclic(encoded)
    
    # Return the final result, which will be the decoded string.
    return decoded