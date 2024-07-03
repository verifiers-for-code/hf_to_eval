def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only's ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    # Initialize the sum to 0
    sum_ascii = 0

    # Iterate through each character in the string
    for char in s:
        # Check if the character is uppercase
        if char.isupper():
            # Add the ASCII code of the uppercase character to the sum
            sum_ascii += ord(char)

    # Return the final sum
    return sum_ascii