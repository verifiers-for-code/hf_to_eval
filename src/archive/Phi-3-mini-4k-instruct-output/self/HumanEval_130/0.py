def tri(n):
    """Returns the first n+1 numbers of the Tribonacci sequence."""
    # Step 1: Define base cases
    if n == 1:
        return [3]
    elif n == 2:
        return [3, 2]
    
    # Step 2: Handle even values of n
    if n % 2 == 0:
        sequence = [3, 2]
        for i in range(2, n):
            next_value = sequence[i-1] + sequence[i-2]
            sequence.append(next_value)
        return sequence
    
    # Step 3: Handle odd values of n
    sequence = [3, 2]
    for i in range(2, n):
        if i % 2 == 0:
            next_value = sequence[i-1] + sequence[i-2]
        else:
            next_value = sequence[i-2] + sequence[i-1] + sequence[i-1]
        sequence.append(next_value)
    
    # Step 4: Optimize and reduce redundant calculations
    # This step is already handled in the previous steps
    
    # Step 5: Output the sequence array
    return sequence