def encode_cyclic(s: str) -> str:
    """
    Encodes a string by cycling groups of 3 characters twice.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    result = ""
    for i in range(0, len(s), 3):
        group = s[i:i+3]
        if len(group) < 3:
            group += " " * (3 - len(group))
        result += group * 2
    return result

def decode_cyclic(s: str) -> str:
    """
    Decodes a string encoded with the encode_cyclic function.
    
    Parameters:
    s (str): The input string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    # Step 3: Call the encode_cyclic function on the input string 's'
    encoded_s = encode_cyclic(s)
    
    # Step 4: Call the encode_cyclic function again on the result of step 3
    decoded_s = encode_cyclic(encoded_s)
    
    # Step 5: Return the final result, which will be the decoded string
    return decoded_s