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
    1. Define the base cases:
        - fibfib(0) == 0
        - fibfib(1) == 0
        - fibfib(2) == 1
    
    2. Set up a dynamic programming approach:
        - Create a list to store the FibFib numbers
        - Initialize the list with the base cases
    
    3. Implement the recursive formula:
        - Use a loop to calculate the FibFib numbers from 3 to n
        - For each number, calculate the FibFib value using the formula:
            fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
        - Store the calculated value in the list
    
    4. Handle edge cases:
        - Check if n is less than 0 and raise an error if true
    
    5. Return the result:
        - Return the n-th FibFib number from the list
    
    Note: Consider using a more efficient approach, such as memoization or dynamic programming, to avoid redundant calculations."""
    
    # Step 1: Define the base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Step 2: Set up a dynamic programming approach
    fibfib_list = [0, 0, 1]
    
    # Step 3: Implement the recursive formula
    for i in range(3, n+1):
        fibfib_list.append(fibfib_list[i-1] + fibfib_list[i-2] + fibfib_list[i-3])
    
    # Step 4: Handle edge cases
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Step 5: Return the result
    return fibfib_list[n]