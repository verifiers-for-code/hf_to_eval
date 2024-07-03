from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero, and
    at that point function should return True. Otherwise, it should return False.

    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True

    Action Plan:
    1. Initialize a variable `balance` to 0, representing the starting balance of the bank account.
    2. Iterate through each operation in the `operations` list:
        a. For each operation, add the operation value to the `balance`.
        b. Check if the `balance` becomes negative after the operation.
        c. If the `balance` is negative, immediately return `True` to indicate that the balance has fallen below zero.
    3. If the loop completes without finding a negative balance, return `False` to indicate that the balance has not fallen below zero.

    Note: Use a for loop to iterate through the list of operations.
    Be careful to update the `balance` correctly for each operation.
    Return `True` as soon as a negative balance is detected, and `False` otherwise."""
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False