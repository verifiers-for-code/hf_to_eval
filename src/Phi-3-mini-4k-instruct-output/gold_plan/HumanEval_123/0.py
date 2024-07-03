def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

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
    1. Initialize an empty list to store odd numbers in the Collatz sequence.
    2. Check if the input n is odd. If so, add it to the list.
    3. Implement a loop that continues until n becomes 1:
       a. If n is even, divide it by 2.
       b. If n is odd, multiply it by 3 and add 1.
       c. If the new n is odd, add it to the list.
    4. Ensure that 1 is added to the list if it's not already present.
    5. Sort the list in ascending order.
    6. Return the sorted list of odd numbers.

    Remember to handle edge cases, such as when n is 1 or when n is even.
    """
    odd_collatz = []
    if n % 2 != 0:
        odd_collatz.append(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        if n % 2 != 0:
            odd_collatz.append(n)
    if 1 not in odd_collatz:
        odd_collatz.append(1)
    odd_collatz.sort()
    return odd_collatz