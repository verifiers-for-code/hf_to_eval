def rounded_avg(n, m):
    # Step 1: Check if n is greater than m
    if n > m:
        return -1

    # Step 2: Initialize a variable to store the sum of integers
    total_sum = 0

    # Step 3: Use a loop to iterate from n to m (inclusive) and add each number to the sum
    for i in range(n, m + 1):
        total_sum += i

    # Step 4: Calculate the average by dividing the sum by the count of numbers (m - n + 1)
    avg = total_sum / (m - n + 1)

    # Step 5: Round the average to the nearest integer using the round() function
    rounded_avg = round(avg)

    # Step 6: Convert the rounded average to binary using the bin() function
    binary_result = bin(rounded_avg)

    # Step 7: Return the binary result
    return binary_result