def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    Action Plan:
    1. Create a helper function to decode a single character:
        a. Get the ASCII value of the character
        b. Subtract the ASCII value of 'a' to get the character's position in the alphabet (0-indexed)
        c. Subtract 5 from the position
        d. Use modulo 26 to handle shifts that go past 'a'
        e. Add the ASCII value of 'a' back to the result to get the decoded character's ASCII
        f. Convert the ASCII back to a character
    
    2. Apply the helper function to each character in the encoded string:
        a. Iterate through the string using a list comprehension
        b. Use the helper function on each character
    
    3. Assemble the decoded string:
        a. Join the list of decoded characters into a single string
    
    4. Account for edge cases and shifts beyond the alphabet:
        a. Handle lowercase and uppercase letters separately if needed
        b. Decide on a way to deal with shifts that exceed the alphabet range ('a' - 'z' or 'A' - 'Z')
    
    5. Assessment:
        a. Ensure the decoded string is the same as the original string before encoding
        b. Test with various encoded strings to verify correct decoding
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return encode_shift(s)