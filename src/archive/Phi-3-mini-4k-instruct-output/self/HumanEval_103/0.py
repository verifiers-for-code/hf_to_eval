def rounded_avg(n, m):
    """Compute the average of integers from n to m (inclusive), round the result to the nearest integer, and convert it to binary.
    If n > m, return -1.
    """
    # Input validation
    if n > m:
        return -1

    # Compute the sum of integers from n to m
    total_sum = sum(range(n, m + 1))

    # Calculate the average
    count = m - n + 1
    average = total_sum / count

    # Round the average
    rounded_average = round(average)

    # Convert the rounded average to binary
    binary_representation = bin(rounded_average)

    return binary_representation