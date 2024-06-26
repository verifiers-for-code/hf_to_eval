def digitSum(s):
    """
    Write a function that takes a string as input and returns the sum of the upper characters only's ASCII codes.
    """
    # Step 1: Check if the input string is empty. If so, return 0.
    if not s:
        return 0

    # Step 2: Initialize a variable to store the sum of ASCII codes.
    ascii_sum = 0

    # Step 3: Iterate through each character in the input string
    for char in s:
        # Step 3a: Check if the character is uppercase using a string method
        if char.isupper():
            # Step 3b: Convert the character to its ASCII code using the ord() function
            ascii_sum += ord(char)

    # Step 4: After the iteration, return the final sum.
    return ascii_sum