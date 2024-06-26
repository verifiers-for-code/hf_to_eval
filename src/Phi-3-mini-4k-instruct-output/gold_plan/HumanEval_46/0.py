def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    """
    # Step 1: Initialize a list with the first four elements of the sequence
    sequence = [0, 0, 2, 0]

    # Step 2: Check if n is less than 4
    if n < 4:
        return sequence[n]

    # Step 3: Implement an iterative approach
    for i in range(4, n + 1):
        # Calculate the new element by summing the four elements in the list
        new_element = sum(sequence[-4:])
        # Append the new element to the end of the list
        sequence.append(new_element)
        # Remove the first (oldest) element from the list
        sequence.pop(0)

    # Step 4: Return the last element of the list as the result
    return sequence[-1]