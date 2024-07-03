def is_simple_power(x, n):
    """
    Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    
    1. Handle edge cases:
       a. If n is less than or equal to 1, return False (x cannot be a power of n)
       b. If n is 1, return True (x is a power of 1)
       c. If x is 1, return True (1 is a power of any number)
    
    2. Implement the logic to check if x is a power of n:
       a. Initialize a variable to store the power (set to 1)
       b. While x is greater than 1 and n raised to the power is less than or equal to x:
          - Increment the power by 1
          - Divide x by n raised to the power
       c. If x becomes 1, return True (x is a power of n)
       d. If x is not equal to 1, return False (x is not a power of n)
    
    3. Return the result:
       a. Based on the above logic, return True if x is a power of n, False otherwise
    
    Additional implementation details:
    - Use a while loop to repeatedly divide x by n raised to the power until x becomes 1 or not divisible
    - Use the ** operator to raise n to the power
    - Ensure that the function handles negative numbers and zero correctly
    - Consider adding input validation to ensure x and n are positive integers
    """
    if n <= 1:
        return False
    if n == 1:
        return True
    if x == 1:
        return True
    
    power = 1
    while x > 1 and n ** power <= x:
        x //= n ** power
        power += 1
    
    return x == 1