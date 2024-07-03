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
    1. Define the function `tri(n)` that takes a non-negative integer `n` as input.
    2. Initialize a list `sequence` with the base cases: `tri(1) = 3` and `tri(2) = 2`.
    3. Implement a loop to calculate the Tribonacci sequence up to `n + 1` terms:
        a. For each iteration, check if `n` is even or odd.
        b. If `n` is even:
            - Calculate the next term using the formula `tri(n) = 1 + n / 2`.
        c. If `n` is odd:
            - Calculate the next term using the formula `tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1)`.
        d. Append the calculated term to the `sequence` list.
    4. Handle edge cases:
        - If `n` is less than 1, return an empty list.
    5. Return the final `sequence` list containing the first `n + 1` terms of the Tribonacci sequence."""

    if n < 1:
        return []

    sequence = [3, 2]

    for i in range(2, n + 1):
        if i % 2 == 0:
            next_term = 1 + i / 2
        else:
            next_term = sequence[i - 1] + sequence[i - 2] + sequence[i + 1]
        sequence.append(next_term)

    return sequence