def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    

    Action Plan:
    1. Initialize a list to store the Fib4 sequence with the first four elements predefined based on the problem statement
    
    2. Use a loop to compute the values beyond the initial predefined four elements:
        a. Start the loop from index 4, iterating up to the given 'n'
        b. For each iteration, compute the next value by summing the last four elements in the sequence
    
    3. Return the n-th element of the sequence
    
    4. Edge cases to consider:
        a. n=0, n=1, and n=2, where the sequence values are already defined
        b. n larger than the predefined sequence (consider adding more elements if necessary)
    
    5. Optimization:
        a. Avoid recalculations by using previously computed values
        b. The iterative approach is more space-efficient than storing the entire sequence
    
    6. Remember to return the value in the correct order (nth element)"""
    
    # Step 1: Initialize the Fib4 sequence with the first four elements
    fib4_sequence = [0, 0, 2, 0]
    
    # Step 2: Compute the values beyond the initial four elements
    for i in range(4, n+1):
        # Compute the next value by summing the last four elements
        next_value = fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4]
        # Append the next value to the sequence
        fib4_sequence.append(next_value)
    
    # Step 3: Return the n-th element of the sequence
    return fib4_sequence[n]