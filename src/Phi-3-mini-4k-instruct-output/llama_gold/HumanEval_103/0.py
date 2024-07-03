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
    1. Check if n is greater than m. If true, return -1 immediately.
    2. Initialize a variable to store the sum of integers from n to m.
    3. Iterate from n to m (inclusive) and add each integer to the sum variable.
    4. Calculate the average by dividing the sum by the number of integers (m - n + 1).
    5. Round the average to the nearest integer using a suitable rounding function.
    6. Convert the rounded average to a binary string using a suitable conversion function.
    7. Return the binary string as the result.
    
    Note: Be mindful of the binary string format, which should start with "0b" followed by the binary digits."""
    
    if n > m:
        return -1
    
    sum_of_integers = sum(range(n, m+1))
    num_of_integers = m - n + 1
    average = round(sum_of_integers / num_of_integers)
    
    binary_string = bin(average)
    
    return binary_string