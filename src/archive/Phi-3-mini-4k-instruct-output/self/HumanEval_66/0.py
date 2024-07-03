def digitSum(s):
    """Returns the sum of the ASCII codes of uppercase characters in the input string."""
    # Initialize the sum variable to 0
    sum_ascii = 0
    
    # Iterate over each character in the input string
    for char in s:
        # Check if a character is uppercase
        if ord(char) >= 65 and ord(char) <= 90:
            # Add its ASCII value to the sum
            sum_ascii += ord(char)
    
    # Return the sum of ASCII values
    return sum_ascii