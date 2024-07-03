def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    

    1. Define the function and its parameters:
       - The function takes a single parameter 'decimal' of type int
       - The function returns a string representing the binary representation of the decimal number
    
    2. Convert the decimal number to binary:
       - Use the built-in bin() function to convert the decimal number to a binary string
       - The resulting string will have a '0b' prefix, which needs to be removed
    
    3. Remove the 'db' characters from the binary representation:
       - Use string slicing to remove the first two characters ('db') from the binary string
       - This will leave only the binary digits (0s and 1s) in the string
    
    4. Return the resulting binary string:
       - The final string will contain only the binary digits, without the 'db' characters
       - This string represents the binary representation of the input decimal number
    
    Additional implementation details:
    - Use the bin() function to convert the decimal number to binary
    - Use string slicing to remove the 'db' characters from the binary string
    - Ensure that the function handles decimal numbers of various sizes correctly
    - Consider adding input validation to handle invalid decimal numbers"""
    if not isinstance(decimal, int):
        raise ValueError("Input must be an integer")
    binary_str = bin(decimal)[2:]
    return "db" + binary_str + "db"