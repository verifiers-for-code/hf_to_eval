def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    # Step 1: Define the base cases for the Fibonacci sequence
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Step 2: Understand the recursive formula
    # The n-th Fibonacci number is the sum of the (n-1)th and (n-2)th Fibonacci numbers
    
    # Step 3: Implement the fib function
    # Handle the base cases (n == 0 and n == 1) by returning the corresponding values
    # For n > 1, recursively call the fib function with n-1 and n-2, and return the sum of the results
    return fib(n-1) + fib(n-2)

# Step 4: Consider handling edge cases and inputs
# Ensure the function can handle non-integer inputs or negative numbers (e.g., by raising an error or returning an error message)