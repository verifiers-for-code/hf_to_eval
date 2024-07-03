def decimal_to_binary(decimal):
    # Step 1: Check for edge cases
    if decimal < 0:
        return "Error: Negative numbers are not valid for binary conversion."
    if not isinstance(decimal, int):
        return "Error: Input must be a non-negative integer."

    # Step 2: Initialize an empty string to store the binary representation
    binary_str = ""

    # Step 3: Implement the conversion logic using a loop
    while decimal > 0:
        remainder = decimal % 2
        binary_str = str(remainder) + binary_str
        decimal = decimal // 2

    # Step 4: Add 'db' to both ends of binary_str
    binary_str = "db" + binary_str + "db"

    # Step 5: Return the resulting string
    return binary_str