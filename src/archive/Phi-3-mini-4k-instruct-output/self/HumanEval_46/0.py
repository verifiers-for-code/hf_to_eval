def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    """
    # Step 1: Initialize a list to store the Fib4 sequence with the first four elements predefined based on the problem statement
    fib4_sequence = [0, 0, 2, 0]
    
    # Step 2: Use a loop to compute the values beyond the initial predefined four elements
    for i in range(4, n + 1):
        # For each iteration, compute the next value by summing the last four elements in the sequence
        next_value = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]
        fib4_sequence.append(next_value)
    
    # Step 3: Return the n-th element of the sequence
    return fib4_sequence[n]