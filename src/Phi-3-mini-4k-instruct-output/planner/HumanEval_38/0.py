def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    

    Action Plan:
    1. Split the input string into groups of three characters, except for the last group which may have fewer than three characters.
    2. Initialize an empty list to store the decoded characters.
    3. Iterate through each group:
        a. If the group has three characters, reverse the order of the characters in the group.
        b. If the group has fewer than three characters, add the characters to the decoded list as they are.
    4. Join the decoded characters into a single string.
    5. Return the decoded string.
    
    Note: Be careful when handling the last group, as it may have fewer than three characters.
    Use appropriate string slicing and concatenation operations to reverse the cycling process."""
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
    groups = [(group[-1] + group[1:-1] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)