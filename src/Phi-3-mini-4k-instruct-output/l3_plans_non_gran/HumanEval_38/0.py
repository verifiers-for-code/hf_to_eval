def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    

    Action Plan:
    1. Understand the encoding process:
        - The encode_cyclic function splits the input string into groups of three characters.
        - Each group is cycled to create a new group, except for groups with fewer than three characters.
        - The cycled groups are then joined to form the encoded string.
    
    2. Identify the pattern in the encoded string:
        - Observe that each group in the encoded string is a cyclic permutation of the corresponding group in the original string.
        - The first character of each group is now at the end, and the last character is at the beginning.
    
    3. Decode the string by reversing the pattern:
        - Iterate through each group in the encoded string.
        - For each group, extract the last character and move it to the beginning.
        - Then, extract the remaining characters and move them to the end.
    
    4. Return the decoded string:
        - Join the decoded groups together to form the final decoded string.
    
    Note: Pay attention to the indexing and slicing operations when decoding the string.
    Ensure that the decoding process correctly reverses the pattern introduced by the encoding process.
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
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)