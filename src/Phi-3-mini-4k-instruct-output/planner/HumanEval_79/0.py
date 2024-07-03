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
    1. Define the function `decimal_to_binary` with a single parameter `decimal`.
    2. Convert the input `decimal` number to binary using the built-in `bin()` function.
    3. Remove the '0b' prefix from the binary string using string slicing.
    4. Add the extra characters 'db' at the beginning and end of the binary string.
    5. Return the final string with the binary representation.
    
    Note: The `bin()` function returns a string that starts with '0b', so we need to remove this prefix.
    The extra characters 'db' are added to the string to meet the specified format."""

    binary_string = bin(decimal)[2:]
    final_string = 'db' + binary_string + 'db'
    return final_string