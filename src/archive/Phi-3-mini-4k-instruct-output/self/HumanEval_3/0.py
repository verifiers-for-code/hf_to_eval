from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero, and
    at that point function should return True. Otherwise, it should return False.

    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    # Step 1: Initialize account_balance to 0
    account_balance = 0

    # Step 2: Iterate through the operations list using a for loop
    for operation in operations:
        # Step 3: Check the current operation's value
        if operation > 0:
            # If the value is positive, it's a deposit: add it to account_balance
            account_balance += operation
        elif operation < 0:
            # If the value is negative, it's a withdrawal: subtract it from account_balance
            account_balance -= operation

        # Step 4: After updating the balance, check if it's below zero
        if account_balance < 0:
            # If yes, set a flag to True and break the loop
            return True

    # Step 5: After the loop ends, check the flag
    return False