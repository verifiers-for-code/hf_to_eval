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
    

    1. Handle the base cases:
       - If n is 0, return 0
       - If n is 1, return 0
       - If n is 2, return 2
       - If n is 3, return 0
    
    2. Initialize the first four elements of the sequence:
       - fib4_0 = 0
       - fib4_1 = 0
       - fib4_2 = 2
       - fib4_3 = 0
    
    3. Compute the remaining elements using a loop:
       - Start the loop from 4 (since we already have the first four elements)
       - For each iteration:
         a. Calculate the next element as the sum of the previous four elements (fib4_n-1 + fib4_n-2 + fib4_n-3 + fib4_n-4)
         b. Update the previous four elements by shifting them to the right (fib4_n-1 becomes fib4_n-2, and so on)
    
    4. Return the n-th element:
       - After the loop, fib4_n will hold the n-th element of the Fib4 sequence
       - Return fib4_n
    
    Additional implementation details:
    - Use a for loop to iterate from 4 to n (inclusive)
    - Use the correct indexing to access the previous four elements in the loop
    - Ensure that the function handles invalid input values (e.g., negative numbers) correctly"""
    
    if n < 0:
        raise ValueError("Input value must be non-negative")
    
    fib4_0, fib4_1, fib4_2, fib4_3 = 0, 0, 2, 0
    
    for i in range(4, n+1):
        fib4_n = fib4_0 + fib4_1 + fib4_2 + fib4_3
        fib4_0, fib4_1, fib4_2, fib4_3 = fib4_1, fib4_2, fib4_3, fib4_n
    
    return fib4_n