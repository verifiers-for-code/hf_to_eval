def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    Action Plan:
    1. Initialize an empty result string to store the decoded characters.
    2. Iterate through each character in the input string 's':
        a. Convert the character to its ASCII value using ord().
        b. Subtract 5 from the ASCII value to shift it back.
        c. Subtract the ASCII value of 'a' to get a number between 0 and 25.
        d. Use modulo 26 to handle wrap-around cases (e.g., 'a' -> 'v').
        e. Add the ASCII value of 'a' to get back to the correct ASCII range.
        f. Convert the resulting ASCII value back to a character using chr().
        g. Append the decoded character to the result string.
    3. Return the final result string containing all decoded characters.
    
    Hint: The implementation will be very similar to encode_shift, but with '-5' instead of '+5'.
    """
    result = ""
    for char in s:
        ascii_val = ord(char)
        shifted_val = (ascii_val - 5 - ord('a')) % 26 + ord('a')
        result += chr(shifted_val)
    return result