def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in Collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.

    Action Plan:
    1. Define a function `get_odd_collatz` that takes a positive integer `n` as input.
    2. Initialize an empty list `collatz_sequence` to store the Collatz sequence.
    3. Implement a loop that generates the Collatz sequence:
        a. Start with `n` and iterate until `n` becomes 1.
        b. In each iteration, check if `n` is even or odd:
            - If even, divide `n` by 2.
            - If odd, multiply `n` by 3 and add 1.
        c. Add the current `n` to the `collatz_sequence` list.
    4. Filter out the odd numbers from the `collatz_sequence` list:
        a. Use a list comprehension to create a new list `odd_numbers` that only contains the odd numbers from `collatz_sequence`.
    5. Sort the `odd_numbers` list in increasing order.
    6. Return the sorted `odd_numbers` list as the result.
    """
    collatz_sequence = []
    while n != 1:
        collatz_sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        collatz_sequence.append(n)

    odd_numbers = [num for num in collatz_sequence if num % 2 != 0]
    odd_numbers.sort()

    return odd_numbers