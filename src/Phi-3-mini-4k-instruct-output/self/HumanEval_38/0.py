def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    
    Action Plan:
    1. Split the input string into groups, each containing three characters or less (considering zero-indexing)
    
    2. Iterate through each group in the input string:
        a. For groups with exactly three characters, cycle the characters the usual way (move the last character to the front)
    
    3. For groups with less than three characters:
        a. Cycle the characters to form a full group of three by repeating the characters at the end (e.g., 'abc' -> 'bcaa', 'cab' -> 'caba')
    
    4. Combine all groups into a single string
    
    5. Testing:
        a. Verify that the decoded string matches the original string
        b. Check edge cases, such as empty input and strings with only one or two characters
    
    6. Comment your code to clarify the logic used for the cycling operation and its inversion for decoding
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group + group[:2] for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group[:-2] + group[-1] for group in groups]
    return "".join(groups)


# Testing
original_string = "abcdefgh"
encoded_string = encode_cyclic(original_string)
decoded_string = decode_cyclic(encoded_string)

assert original_string == decoded_string, "The decoded string does not match the original string."

# Check edge cases
assert encode_cyclic("") == "", "Empty string should return an empty string."
assert encode_cyclic("a") == "a", "Single character string should remain the same."
assert encode_cyclic("ab") == "ba", "Two character string should be cycled."
assert decode_cyclic("a") == "a", "Decoding single character string should return the same string."
assert decode_cyclic("ba") == "ab", "Decoding two character string should return the original string."