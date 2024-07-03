from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True

    Action Plan:
    1. Initialize a variable to keep track of the account balance, starting at zero.
    2. Loop through each operation in the 'operations' list:
       a. Update the balance by adding the current operation (positive for deposits, negative for withdrawals).
       b. Check if the balance has become negative:
          - If yes, immediately return True as the balance has fallen below zero.
    3. If the loop completes without returning True, it means the balance never fell below zero.
    4. Return False after the loop ends.

    Remember:
    - Positive numbers in 'operations' represent deposits (increasing balance).
    - Negative numbers in 'operations' represent withdrawals (decreasing balance).
    - The function should return as soon as the balance becomes negative, not at the end of all operations.
    """

    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False