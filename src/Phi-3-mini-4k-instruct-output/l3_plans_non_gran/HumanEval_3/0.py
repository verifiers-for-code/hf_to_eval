from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero, and
    at that point function should return True. Otherwise it should return False.
    
    Action Plan:
    1. Initialize the balance to zero.
    2. Create a loop to iterate through each operation in the list of operations.
    3. Inside the loop, apply each operation to the balance:
        a. If the operation is a deposit, add it to the balance.
        b. If the operation is a withdrawal, subtract it from the balance.
    4. After applying each operation, check if the balance has fallen below zero.
    5. If the balance is below zero, return True immediately.
    6. If the loop completes without the balance falling below zero, return False.
    """
    balance = 0
    for operation in operations:
        if operation > 0:
            balance += operation
        else:
            balance -= abs(operation)
        if balance < 0:
            return True
    return False