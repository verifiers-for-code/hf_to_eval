def digitSum(s):
    """
    Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153

    Action Plan:
    1. Iterate over each character in the input string using a loop or a comprehension
    2. Check if a character is uppercase by comparing its ASCII value using `ord()` function
    3. If a character is uppercase, add its ASCII value to the sum
    4. Initialize the sum variable to 0 before iterating
    5. Implement handling of the edge case where the input string is empty
    6. Review and validate test cases to ensure correctness and robustness of the implementation
    """
    # Initialize the sum variable to 0
    sum_upper_chars = 0

    # Iterate over each character in the input string
    for char in s:
        # Check if the character is uppercase
        if ord(char) > 64 and ord(char) < 91:
            # Add the ASCII value of the uppercase character to the sum
            sum_upper_chars += ord(char)

    # Return the sum of the upper characters' ASCII values
    return sum_upper_chars