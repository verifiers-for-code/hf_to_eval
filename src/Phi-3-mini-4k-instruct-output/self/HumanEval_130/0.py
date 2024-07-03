def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    

    Action Plan:
    1. Define the base cases for n = 1 and n = 2.
        - tri(1) returns 3
        - tri(2) calculates and returns 2
    
    2. Handle even values of n efficiently.
        - For even n, iterate from n down to 2 and calculate tri(i) based on the given formula.
    
    3. Handle odd values of n and avoid deep recursion for n >= 2.
        - Initialize an array to store the sequence.
        - Use a loop to calculate tri(n) based on the recurrence relation for odd n.
        - Ensure tri(n-2) and tri(n-1) are already calculated before calculating tri(n).
    
    4. Optimize and reduce redundant calculations within the loop.
        - Store each value in the sequence array after calculation to be used in subsequent iterations.
    
    5. Output the sequence array with the first n + 1 elements."""
    
    # Step 1: Base cases
    if n == 1:
        return [3]
    elif n == 2:
        return [3, 2]
    
    # Step 2: Handle even values of n
    sequence = [3, 2]
    for i in range(3, n + 1):
        if i % 2 == 0:
            sequence.append(1 + i // 2)
    
    # Step 3: Handle odd values of n
    for i in range(n + 1, n + 2):
        if i % 2 != 0:
            sequence.append(sequence[-1] + sequence[-2] + sequence[-3])
    
    # Step 4: Optimize and reduce redundant calculations
    # (Already handled in the above steps)
    
    # Step 5: Output the sequence array with the first n + 1 elements
    return sequence