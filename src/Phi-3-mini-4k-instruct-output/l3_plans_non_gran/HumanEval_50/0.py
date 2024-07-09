def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    

    Action Plan:
    1. Understand the encoding process:
        - The encode_shift function shifts every character by 5 in the alphabet.
        - It uses the ASCII value of characters and the modulus operator to ensure wrapping around the alphabet.
    
    2. Identify the decoding process:
        - To decode, we need to reverse the encoding process.
        - This involves subtracting 5 from the ASCII value of each character and taking the modulus 26 to wrap around the alphabet.
    
    3. Apply the inverse operation:
        - Use a list comprehension or a loop to iterate over each character in the encoded string.
        - For each character, subtract 5 from its ASCII value and take the modulus 26.
        - Convert the resulting ASCII value back to a character using the chr function.
    
    4. Handle edge cases:
        - Consider characters that are not alphabets (e.g., spaces, punctuation, digits).
        - Decide how to handle these characters (e.g., leave them unchanged, raise an error).
    
    5. Return the decoded string:
        - Join the decoded characters into a single string using the join method.
        - Return the resulting decoded string."""
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])