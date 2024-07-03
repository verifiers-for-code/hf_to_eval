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
    1. Check if n is greater than m. If so, return -1.
    2. Initialize a variable to store the sum of integers.
    3. Use a loop to iterate from n to m (inclusive) and add each number to the sum.
    4. Calculate the average by dividing the sum by the count of numbers (m - n + 1).
    5. Round the average to the nearest integer using the round() function.
    6. Convert the rounded average to binary using the bin() function.
    7. Return the binary result.
    """
    if n > m:
        return -1
    else:
        sum_of_integers = sum(range(n, m+1))
        count_of_numbers = m - n + 1
        average = sum_of_integers / count_of_numbers
        rounded_average = round(average)
        binary_result = bin(rounded_average)
        return binary_result