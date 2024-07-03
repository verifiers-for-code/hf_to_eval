def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    1. Understand the encoding process:
       - The encode_shift function shifts every character in the input string by 5 in the alphabet
       - This is done using a simple arithmetic operation on the ASCII values of the characters
    
    2. Reverse the encoding process:
       - To decode the string, we need to shift the characters back by 5 in the alphabet
       - This is essentially the same operation as the encoding process, but in reverse
    
    3. Handle non-alphabetic characters:
       - The encode_shift function ignores non-alphabetic characters, such as spaces, punctuation, and digits
       - The decode_shift function should also ignore these characters and leave them unchanged in the decoded string
    
    4. Preserve the original case of the characters:
       - The encode_shift function does not change the case of the characters
       - The decode_shift function should also preserve the original case of the characters
    
    Implementation details:
    - Use a similar approach to the encode_shift function, but with a negative shift of -5 instead of 5
    - Use the same ASCII offset for lowercase and uppercase letters (ord("a") and ord("A"))
    - Ensure that the function handles empty input strings correctly
    - Consider adding error handling for non-string inputs
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])