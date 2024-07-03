def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    """
    # Initialize the first four elements of the sequence
    fib4_sequence = [0, 0, 2, 0]
    
    # Compute the remaining elements of the sequence
    for i in range(4, n+1):
        fib4_sequence.append(fib4_sequence[i-1] + fib4_sequence[i-2] + fib4_sequence[i-3] + fib4_sequence[i-4])
    
    # Return the n-th element of the sequence
    return fib4_sequence[n]