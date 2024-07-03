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
    1. Use a built-in function to convert the decimal number to a binary string.
    2. Remove the prefix from the binary string (if it exists).
    3. Add the 'db' prefix and suffix to the binary string.
    4. Return the resulting string, which should start and end with 'db' and contain the binary representation of the input decimal number."""
    
    # Step 1: Convert the decimal number to a binary string
    binary_string = bin(decimal)[2:]
    
    # Step 2: Remove the prefix from the binary string (if it exists)
    # Since the prefix 'db' is not part of the binary representation, we can skip this step.
    
    # Step 3: Add the 'db' prefix and suffix to the binary string
    result_string = 'db' + binary_string + 'db'
    
    # Step 4: Return the resulting string
    return result_string