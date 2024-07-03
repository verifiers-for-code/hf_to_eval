from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    balance = 0  # Step 1: Initialize a variable to keep track of the account balance, starting at zero.

    for operation in operations:  # Step 2: Loop through each operation in the 'operations' list.
        balance += operation  # Update the balance by adding the current operation.
        if balance < 0:  # Step 2b: Check if the balance has become negative.
            return True  # If yes, immediately return True.

    return False  # Step 3: If the loop completes without returning True, it means the balance never fell below zero.