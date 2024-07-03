def fib4(n: int) -> int:
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence. 
    Do not use recursion.

    Args:
    n (int): The index of the element in the fib4 sequence to compute.

    Returns:
    int: The n-th element of the fib4 sequence.

    Action Plan:
    1. Initialize a list `fib4` with the first four elements of the sequence: [0, 0, 2, 0].
    2. Create a loop that iterates from 4 to n (inclusive).
    3. In each iteration:
        a. Calculate the next element by summing the previous four elements in the `fib4` list.
        b. Append the calculated element to the `fib4` list.
    4. After the loop, return the n-th element of the `fib4` list.
    5. Test the function with the provided examples to ensure correctness.

    Note: Use a list to store the sequence and update it iteratively to avoid recursion."""
    fib4_sequence = [0, 0, 2, 0]
    for i in range(4, n + 1):
        next_element = fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4]
        fib4_sequence.append(next_element)
    return fib4_sequence[n]