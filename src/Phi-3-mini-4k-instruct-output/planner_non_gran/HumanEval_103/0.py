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
    

    Action Plan:
    1. Validate the input:
        - Check if n and m are positive integers
        - If not, return -1
    
    2. Calculate the average:
        - Use the formula (n + m) / 2 to find the average
    
    3. Round the average:
        - Use the round() function to round the average to the nearest integer
    
    4. Convert the rounded average to binary:
        - Use the bin() function to convert the rounded average to a binary string
        - Remove the '0b' prefix from the binary string
    
    5. Return the binary representation of the rounded average
    
    Note: Handle edge cases, such as when n is greater than m, by returning -1."""
    
    # Step 1: Validate the input
    if not (isinstance(n, int) and isinstance(m, int) and n > 0 and m > 0):
        return -1
    
    # Step 2: Calculate the average
    avg = (n + m) / 2
    
    # Step 3: Round the average
    rounded_avg = round(avg)
    
    # Step 4: Convert the rounded average to binary
    binary_avg = bin(rounded_avg)[2:]
    
    # Step 5: Return the binary representation of the rounded average
    return binary_avg