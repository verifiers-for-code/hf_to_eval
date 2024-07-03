def decimal_to_binary(decimal):
    """
    Convert a decimal number to binary format.

    Args:
    decimal (int): The decimal number to be converted.

    Returns:
    str: A string representing the binary number with 'db' at the beginning and end.

    Examples:
    >>> decimal_to_binary(15)
    'db1111db'
    >>> decimal_to_binary(32)
    'db100000db'
    """
    # Step 2: Convert the input decimal number to binary using the built-in bin() function
    binary_str = bin(decimal)
    
    # Step 3: Remove the '0b' prefix from the binary string using string slicing
    binary_str = binary_str[2:]
    
    # Step 4: Add the extra characters 'db' at the beginning and end of the binary string
    binary_str = 'db' + binary_str + 'db'
    
    # Step 5: Return the final string with the binary representation
    return binary_str