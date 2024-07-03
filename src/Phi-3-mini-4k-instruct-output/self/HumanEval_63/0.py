def fibfib(n: int, memo={}):
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
    1. Base Case Function:
        a. Check if 'n' is 0 or 1 and return 0 for both
    
    2. Recursive Function:
        a. If 'n' > 1, use a recursive formula taking into account previous three FibFib numbers
    
    3. Consider Memoization:
        a. Implement a dictionary to store already computed FibFib numbers
        b. Check the dictionary before running the recursive function to save computation time
    
    4. Write the function considering the base cases and recursive step, with memoization if necessary
    
    5. Address Edge Cases:
        a. Include input validation to handle non-integer values
        b. Return an appropriate message for n < 0, assuming the sequence might not make logical sense for negative values
    
    6. Finalize the function and test with multiple values of 'n' to ensure correctness and efficiency"""

    # Input validation
    if not isinstance(n, int):
        return "Error: Input must be an integer."
    if n < 0:
        return "Error: FibFib sequence is not defined for negative values."

    # Base cases
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1

    # Check memoization dictionary
    if n in memo:
        return memo[n]

    # Recursive step with memoization
    memo[n] = fibfib(n-1, memo) + fibfib(n-2, memo) + fibfib(n-3, memo)
    return memo[n]