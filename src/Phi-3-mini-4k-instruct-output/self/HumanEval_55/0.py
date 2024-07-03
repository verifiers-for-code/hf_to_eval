def fib(n: int):
    """
    Return n-th Fibonacci number.
    
    Action Plan:
    1. Initialize variables to track the previous two Fibonacci numbers
        - Set fib_prev to 0 (Fibonacci(0))
        - Set fib_current to 1 (Fibonacci(1))
    
    2. Create a loop to iterate n times:
        a. At each iteration, calculate the next Fibonacci number:
            fib_next = fib_prev + fib_current
        b. Update fib_prev and fib_current:
            fib_prev = fib_current
            fib_current = fib_next
    
    3. Return fib_current, which represents the n-th Fibonacci number after the loop
    
    4. Edge cases to consider:
        - n is less than 1: The function should return fib_current (assuming n starts from 1)
        - n is 0: Should return fib_prev (which is 0)
    
    5. Alternative approaches:
        - Recursion: While not the most efficient for large n, provide a recursive approach for completeness
        - Memoization: Demonstrate an approach for memoizing the Fibonacci function to improve performance
    
    6. Testing:
        - Verify correctness with the given test cases and additional edge cases like very large n
    """
    if n < 1:
        return fib_current
    elif n == 0:
        return fib_prev
    
    fib_prev, fib_current = 0, 1
    for _ in range(n):
        fib_next = fib_prev + fib_current
        fib_prev, fib_current = fib_current, fib_next
    
    return fib_current