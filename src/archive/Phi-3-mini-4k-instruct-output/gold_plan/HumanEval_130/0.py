def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """
    # Step 1: Handle the base case
    if n == 0:
        return [1]

    # Step 2: Initialize the sequence
    sequence = [1, 3]

    # Step 3: Implement the main loop
    for i in range(2, n + 1):
        # Step 4: Calculate terms based on even or odd index
        if i % 2 == 0:
            next_term = 1 + i / 2
        else:
            next_term = sequence[i - 1] + sequence[i - 2] + sequence[i - 1] // 2

        # Step 5: Append each calculated term to the sequence list
        sequence.append(next_term)

    # Step 6: Return the complete sequence list
    return sequence