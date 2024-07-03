def rounded_avg(n, m):
    # Check if n is greater than m
    if n > m:
        return -1

    # Calculate the sum of integers from n to m (inclusive)
    total_sum = sum(range(n, m + 1))

    # Calculate the average and round it to the nearest integer
    average = round(total_sum / (m - n + 1))

    # Convert the rounded average to binary and return
    return bin(average)