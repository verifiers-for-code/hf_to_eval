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
    1. Understand the input:
       - The input 'decimal' is an integer in decimal format.

    2. Convert decimal to binary:
       - Use Python's built-in function bin() to convert the decimal to binary.
       - The bin() function returns a string starting with '0b', which we need to remove.

    3. Format the binary string:
       - Add 'db' to the beginning of the binary string.
       - Add 'db' to the end of the binary string.

    4. Return the final formatted binary string.

    Note: Be careful to remove the '0b' prefix from the bin() function result before adding 'db'.
    """
    binary_string = bin(decimal)[2:]  # Remove the '0b' prefix
    formatted_binary_string = 'db' + binary_string + 'db'
    return formatted_binary_string