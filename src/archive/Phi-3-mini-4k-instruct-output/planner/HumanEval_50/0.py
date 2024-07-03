def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Action Plan:
    
    1. Define the function `encode_shift` that takes a string `s` as input.
    2. Initialize an empty string to store the encoded result.
    3. Iterate through each character `ch` in the input string `s`.
    4. For each character:
        a. Convert the character to its ASCII value using `ord()`.
        b. Add 5 to the ASCII value to shift the character.
        c. Calculate the new ASCII value modulo 26 to handle wrapping around the alphabet.
        d. Add the ASCII value of 'a' to the result to get the new character's ASCII value.
        e. Convert the new ASCII value back to a character using `chr()`.
        f. Add the new character to the encoded result string.
    5. Return the encoded result string.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with `encode_shift` function. Returns decoded string.
    
    Action Plan:
    
    1. Define the function `decode_shift` that takes a string `s` as input.
    2. Initialize an empty string to store the decoded result.
    3. Iterate through each character `ch` in the input string `s`.
    4. For each character:
        a. Convert the character to its ASCII value using `ord()`.
        b. Subtract 5 from the ASCII value to shift the character back.
        c. Calculate the new ASCII value modulo 26 to handle wrapping around the alphabet.
        d. Add the ASCII value of 'a' to the result to get the new character's ASCII value.
        e. Convert the new ASCII value back to a character using `chr()`.
        f. Add the new character to the decoded result string.
    5. Return the decoded result string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])