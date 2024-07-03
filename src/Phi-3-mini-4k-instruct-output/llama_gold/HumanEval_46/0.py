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
    1. Define the base cases of the Fib4 sequence: fib4(0) = 0, fib4(1) = 0, fib4(2) = 2, fib4(3) = 0.
    2. Initialize a data structure (e.g., a list) with these base cases.
    3. If n is less than 4, return the corresponding base case value.
    4. Iterate from 4 to n (inclusive):
       a. Calculate the next value in the sequence by summing the last four values in the data structure.
       b. Add the new value to the end of the data structure.
       c. Remove the oldest value from the beginning of the data structure to maintain a fixed size.
    5. Return the last value in the data structure, which is the nth element of the Fib4 sequence."""
    
    # Step 1: Define the base cases
    fib4_values = [0, 0, 2, 0]
    
    # Step 2: If n is less than 4, return the corresponding base case value
    if n < 4:
        return fib4_values[n]
    
    # Step 3: Iterate from 4 to n (inclusive)
    for i in range(4, n+1):
        # Step 4a: Calculate the next value in the sequence
        next_value = sum(fib4_values)
        
        # Step 4b: Add the new value to the end of the data structure
        fib4_values.append(next_value)
        
        # Step 4c: Remove the oldest value from the beginning of the data structure
        fib4_values.pop(0)
    
    # Step 5: Return the last value in the data structure
    return fib4_values[-1]