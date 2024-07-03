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
    1. Initialize the account balance to zero.
    2. Iterate through each operation in the given list:
       a. Add the operation value to the current balance (positive for deposits, negative for withdrawals).
       b. Check if the updated balance is less than zero.
       c. If the balance is below zero, immediately return True.
    3. If the function hasn't returned True after processing all operations, return False, indicating the balance never fell below zero."""

    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False