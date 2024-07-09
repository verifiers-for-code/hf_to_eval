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
    1. Validate the inputs:
        - Check if n and m are positive integers
        - If n is greater than m, return -1
    
    2. Calculate the sum of integers from n to m:
        - Use the formula for the sum of an arithmetic series to calculate the sum
    
    3. Calculate the average:
        - Divide the sum by the range (m - n + 1)
    
    4. Round the average to the nearest integer:
        - Use the built-in round function to round the average
    
    5. Convert the result to binary:
        - Use the built-in bin function to convert the result to binary
    
    6. Return the final result:
        - Return the binary representation of the rounded average
    
    Note: Be careful with the input validation and edge cases.
    Use the correct formula for the sum of an arithmetic series."""
    
    # Step 1: Validate the inputs
    if not isinstance(n, int) or not isinstance(m, int) or n < 1 or m < 1:
        return "Invalid input"
    if n > m:
        return -1
    
    # Step 2: Calculate the sum of integers from n to m
    sum_n_m = (n + m) * (m - n + 1) // 2
    
    # Step 3: Calculate the average
    avg = sum_n_m / (m - n + 1)
    
    # Step 4: Round the average to the nearest integer
    rounded_avg = round(avg)
    
    # Step 5: Convert the result to binary
    binary_avg = bin(rounded_avg)
    
    # Step 6: Return the final result
    return binary_avg