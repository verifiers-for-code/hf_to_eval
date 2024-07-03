def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    
    1. Understand the encoding process:
       - The encode_cyclic function groups characters of a string into groups of three
       - Each group is then rotated by one character
    
    2. Identify the decoding steps:
       - Split the encoded string into groups of three characters
       - Reverse the rotation process for each group
       - Join the decoded groups back into a single string
    
    3. Implement the decoding logic:
       - Use a list comprehension to split the encoded string into groups
       - For each group, reverse the rotation process by moving the first character to the end
       - Join the decoded groups back into a single string
    
    4. Handle edge cases:
       - Ensure the function handles strings with lengths not divisible by three
       - Consider the case where the input string is empty
    
    5. Implement the decode_cyclic function:
       - Use the decoding logic to process the input string
       - Return the decoded string
    
    Note: The decoding process is essentially the reverse of the encoding process, so the implementation is straightforward.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # reverse the rotation process for each group.
    groups = [group[-1] + group[:-1] if len(group) == 3 else group for group in groups]
    return "".join(groups)