def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    

    1. Check if n is greater than m:
       - If true, return -1 immediately (invalid input)
    
    2. Compute the average of integers from n to m:
       - Use the formula: (m + n) / 2
       - Ensure the result is an integer (e.g., using integer division)
    
    3. Round the average to the nearest integer:
       - Use the built-in round() function
    
    4. Convert the rounded average to binary:
       - Use the built-in bin() function
       - Remove the '0b' prefix from the binary string (e.g., using slicing)
    
    5. Return the binary representation of the rounded average:
       - Ensure the result is a string
    
    Additional implementation details:
    - Use conditional statements (if-else) to handle the edge case where n > m
    - Use arithmetic operations to compute the average of integers from n to m
    - Use the built-in round() and bin() functions to perform the required operations
    - Ensure the function returns a string for the binary representation of the rounded average
    - Consider adding input validation to handle non-integer inputs"""
    if not isinstance(n, int) or not isinstance(m, int):
        return "Invalid input: n and m must be integers"
    if n > m:
        return -1
    avg = (m + n) // 2
    rounded_avg = round(avg)
    binary_avg = bin(rounded_avg)[2:]
    return binary_avg