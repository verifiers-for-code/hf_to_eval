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
    1. Define a function `tri` that takes an integer `n` as input.
    2. Initialize an empty list `tribonacci` to store the Tribonacci sequence.
    3. Calculate the first `n + 1` numbers of the Tribonacci sequence:
        a. Handle even numbers:
            - Calculate `tri(n)` using the formula `1 + n / 2`
            - Append `tri(n)` to the `tribonacci` list
        b. Handle odd numbers:
            - Calculate `tri(n)` using the formula `tri(n - 1) + tri(n - 2) + tri(n + 1)`
            - Append `tri(n)` to the `tribonacci` list
    4. Return the `tribonacci` list containing the first `n + 1` numbers of the Tribonacci sequence.
    5. Consider using a loop to iterate from 1 to `n` to generate the sequence."""
    
    tribonacci = [3]
    for i in range(2, n + 2):
        if i % 2 == 0:
            tribonacci.append(1 + i / 2)
        else:
            tribonacci.append(tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i + 1])
    return tribonacci