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
    1. Initialize an empty list to store the Collatz sequence.
    2. Initialize a variable to keep track of the current number in the sequence, starting with the input number n.
    3. Implement a loop that continues until the current number reaches 1:
        a. Append the current number to the sequence list.
        b. Check if the current number is even:
            - If even, update the current number to half of its current value.
            - If odd, update the current number to 3 times its current value plus 1.
    4. After the loop, filter out even numbers from the sequence list:
        a. Use a list comprehension to create a new list containing only the odd numbers from the sequence.
    5. Return the new list of odd numbers in the Collatz sequence, sorted in increasing order.
    
    Note: Be careful with the sequence generation and filtering logic to ensure correctness."""

    collatz_sequence = []
    current_number = n

    while current_number != 1:
        collatz_sequence.append(current_number)
        if current_number % 2 == 0:
            current_number = current_number // 2
        else:
            current_number = 3 * current_number + 1

    odd_collatz_sequence = [num for num in collatz_sequence if num % 2 != 0]
    return sorted(odd_collatz_sequence)