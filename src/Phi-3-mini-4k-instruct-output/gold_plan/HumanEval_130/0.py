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
    1. Handle the base case:
       - If n is 0, return a list with only the first element [1]

    2. Initialize the sequence:
       - Create a list with the first two elements [1, 3]

    3. Implement the main loop:
       - Iterate from 2 to n (inclusive)

    4. Calculate terms based on even or odd index:
       - For even indices: Use the formula 1 + i / 2
       - For odd indices: Use the formula tri(i-1) + tri(i-2) + tri(i+1)
         Note: For odd indices, tri(i+1) can be calculated as (i+3)/2

    5. Append each calculated term to the sequence list

    6. Return the complete sequence list
    """
    if n == 0:
        return [1]

    sequence = [1, 3]

    for i in range(2, n + 1):
        if i % 2 == 0:
            term = 1 + i / 2
        else:
            term = sequence[i - 1] + sequence[i - 2] + (i + 3) / 2
        sequence.append(term)

    return sequence