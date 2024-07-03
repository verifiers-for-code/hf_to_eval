from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    
    1. Initialize the balance to zero
       - Set a variable (e.g., balance) to 0, which will track the current balance of the bank account
    
    2. Iterate through each operation in the input list:
       - Use a loop to process each operation in the list
    
    3. For each operation:
       a. Check if the operation is a deposit (positive value):
          - Add the operation value to the balance
       b. Check if the operation is a withdrawal (negative value):
          - Subtract the absolute value of the operation from the balance (to handle negative balances)
    
    4. After processing each operation:
       - Check if the balance is less than zero
       - If true, immediately return True (indicating the balance fell below zero)
    
    5. If the loop completes without finding a negative balance:
       - Return False (indicating the balance never fell below zero)
    
    Additional implementation details:
    - Use a for loop to iterate through the list of operations
    - Use an if-elif-else statement to handle the two types of operations (deposit and withdrawal)
    - Use the abs() function to get the absolute value of a negative operation
    - Consider adding input validation to ensure the input list only contains integer values"""

    balance = 0
    for operation in operations:
        if operation > 0:
            balance += operation
        elif operation < 0:
            balance -= abs(operation)
        if balance < 0:
            return True
    return False