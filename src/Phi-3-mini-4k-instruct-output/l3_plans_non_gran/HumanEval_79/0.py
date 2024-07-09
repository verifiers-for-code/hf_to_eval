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
    1. Define a function `decimal_to_binary` that takes a decimal number as input.
    2. Convert the decimal number to binary using the built-in `bin` function.
    3. Remove the '0b' prefix from the binary string.
    4. Remove the 'db' prefix and suffix from the binary string.
    5. Return the resulting binary string.
    6. Consider using string slicing and concatenation to achieve the desired format."""

    binary_string = bin(decimal)[2:]
    return 'db' + binary_string + 'db'