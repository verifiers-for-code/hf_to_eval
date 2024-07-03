def rounded_avg(n, m):
    """
    You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    
    Parameters:
    n (int): The starting integer.
    m (int): The ending integer.
    
    Returns:
    str: The binary representation of the rounded average, or -1 if n > m.
    """
    # Step 1: Validate the input
    if not (isinstance(n, int) and isinstance(m, int) and n > 0 and m > 0):
        return -1
    if n > m:
        return -1
    
    # Step 2: Calculate the average
    average = (n + m) / 2
    
    # Step 3: Round the average
    rounded_average = round(average)
    
    # Step 4: Convert the rounded average to binary
    binary_representation = bin(rounded_average)[2:]
    
    # Step 5: Return the binary representation of the rounded average
    return binary_representation