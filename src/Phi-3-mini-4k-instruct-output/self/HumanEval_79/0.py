def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    

    Action Plan:
    1. Check for edge cases:
        a. If the decimal is negative, return an error message since it's invalid for binary conversion.
        b. Verify the input is a non-negative integer.
    
    2. Initialize an empty string, binary_str, to store the binary representation.
    
    3. Implement the conversion logic using a loop (e.g., a while loop):
        a. In each iteration, divide the decimal number by 2.
        b. Append the remainder ('0' or '1') to binary_str.
        c. Update decimal number with the quotient.
    
    4. After the loop concludes (when the decimal number is 0), add 'db' to both ends of binary_str.
    
    5. Return the resulting string.
    
    6. Account for cases when decimal number is a large number that could cause an integer overflow if processed in a loop. However, Python's built-in methods can handle this without explicit checks.
    
    7. Test the function with the provided examples and edge cases to ensure correctness."""

    # Check for edge cases
    if decimal < 0:
        return "Error: Negative numbers cannot be converted to binary."

    # Initialize an empty string to store the binary representation
    binary_str = ""

    # Implement the conversion logic using a loop
    while decimal > 0:
        binary_str = str(decimal % 2) + binary_str
        decimal //= 2

    # Add 'db' to both ends of binary_str
    binary_str = "db" + binary_str + "db"

    # Return the resulting string
    return binary_str