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
    1. Handle the base case: If n is 0, return a list containing only 1.
    2. Initialize a list to store the Tribonacci sequence with the first two elements: [1, 3].
    3. Iterate from 2 to n (inclusive):
       a. If the current number is even:
          - Calculate the next Tribonacci number as (i / 2) + 1.
          - Append this number to the Tribonacci sequence list.
       b. If the current number is odd:
          - Calculate the next Tribonacci number using the recurrence formula:
            tri(i) = tri(i - 1) + tri(i - 2) + tri(i + 1) (with adjustments for indexing).
          - Append this number to the Tribonacci sequence list.
    4. Return the final Tribonacci sequence list containing n + 1 numbers."""

    if n == 0:
        return [1]

    tribonacci = [1, 3]

    for i in range(2, n + 1):
        if i % 2 == 0:
            next_num = (i // 2) + 1
        else:
            next_num = tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i + 1]
        tribonacci.append(next_num)

    return tribonacci