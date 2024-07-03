def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24

    Action Plan:
    1. Handle the base cases:
       - If n is 0 or 1, return 0
       - If n is 2, return 1
    
    2. For n > 2, implement the recursive formula:
       fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
    
    3. Consider efficiency improvements:
       - The current recursive solution is not efficient for large n values
       - Consider using memoization to store previously computed values
       - Alternatively, implement an iterative solution using a loop and three variables to store the last three fibfib numbers
    
    4. If using memoization:
       - Create a dictionary or list to store computed fibfib values
       - Check if the value for n is already in the memoization structure before computing
       - Store each computed value in the memoization structure
    
    5. If using an iterative approach:
       - Initialize variables for the first three fibfib numbers: a, b, c = 0, 0, 1
       - Iterate from 3 to n, updating a, b, c at each step
       - Return the final value of c
    
    6. Test the function with the provided example cases and additional edge cases
    """
    # Handle base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Initialize variables for the first three fibfib numbers
    a, b, c = 0, 0, 1
    
    # Iterate from 3 to n
    for i in range(3, n+1):
        # Update a, b, c at each step
        a, b, c = b, c, a + b + c
    
    # Return the final value of c
    return c