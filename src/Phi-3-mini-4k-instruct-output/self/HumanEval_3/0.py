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
    1. Initialize account_balance to 0
    2. Iterate through the operations list using a for loop
    3. In each iteration, check the current operation's value
        a. If the value is positive, it's a deposit: add it to account_balance
        b. If the value is negative, it's a withdrawal: subtract it from account_balance
    4. After updating the balance, check if it's below zero:
        a. If yes, set a flag to True and break the loop
    5. After the loop ends, check the flag:
        a. Return True if the flag is set
        b. Return False otherwise
    6. Test the function with the provided test cases and consider edge cases such as an empty operation list or all operations being zero."""

    account_balance = 0
    below_zero_flag = False

    for operation in operations:
        if operation > 0:
            account_balance += operation
        else:
            account_balance += operation
            if account_balance < 0:
                below_zero_flag = True
                break

    return below_zero_flag