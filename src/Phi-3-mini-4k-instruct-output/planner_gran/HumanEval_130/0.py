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
    1. Initialize the first three numbers of the Tribonacci sequence:
       - Set tri[0] to 3 (the first number in the sequence)
       - Set tri[1] to 3 (the second number in the sequence)
       - Set tri[2] to 3 (the third number in the sequence)
    
    2. Create an empty list to store the sequence:
       - Initialize an empty list called sequence to store the generated sequence
    
    3. Generate the sequence up to the nth number:
       - Use a loop that iterates from 3 to n (inclusive)
       - For each iteration:
         a. Check if the current index is even (i % 2 == 0)
         b. If even, calculate the next number as tri(n) = 1 + n / 2
         c. If odd, calculate the next number as tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1)
         d. Append the calculated number to the sequence list
    
    4. Handle edge cases:
       - Ensure the function works correctly for n = 0, 1, and 2
       - Consider adding input validation for non-negative integers
    
    5. Return the generated sequence:
       - Return the sequence list containing the first n + 1 numbers of the Tribonacci sequence
    
    Additional implementation details:
    - Use a loop to iterate from 3 to n (inclusive)
    - Use the modulus operator (%) to check if the index is even or odd
    - Use list indexing to access and update the sequence numbers
    - Ensure the function returns the correct sequence for different input values"""
    
    # Initialize the first three numbers of the Tribonacci sequence
    tri = [3, 3, 3]
    
    # Create an empty list to store the sequence
    sequence = []
    
    # Generate the sequence up to the nth number
    for i in range(3, n+1):
        if i % 2 == 0:
            # If the current index is even, calculate the next number as tri(n) = 1 + n / 2
            next_num = 1 + i / 2
        else:
            # If the current index is odd, calculate the next number as tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1)
            next_num = tri[i-1] + tri[i-2] + tri[i+1]
        
        # Append the calculated number to the sequence list
        sequence.append(next_num)
    
    # Return the generated sequence
    return sequence