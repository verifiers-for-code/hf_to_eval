def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    def decode_char(ch: str):
        """
        decodes a single character by shifting it back by 5 in the alphabet.
        """
        ascii_val = ord(ch)
        # Get the character's position in the alphabet (0-indexed)
        pos = ascii_val - ord('a')
        # Subtract 5 from the position and use modulo 26 to handle shifts that go past 'a'
        pos = (pos - 5) % 26
        # Add the ASCII value of 'a' back to the result to get the decoded character's ASCII
        decoded_ascii = pos + ord('a')
        # Convert the ASCII back to a character
        return chr(decoded_ascii)

    # Apply the helper function to each character in the encoded string
    decoded_chars = [decode_char(ch) for ch in s]
    # Assemble the decoded string
    decoded_str = "".join(decoded_chars)
    return decoded_str