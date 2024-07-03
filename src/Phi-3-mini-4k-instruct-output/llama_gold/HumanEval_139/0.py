def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    

    Action Plan:
    1. Initialize a variable to store the running product of the special factorial (initially set to 1).
    2. Initialize a variable to store the current factorial (initially set to 1).
    3. Iterate from 1 to the input number (n):
       a. Calculate the factorial of the current number by multiplying the current number with the previous factorial.
       b. Multiply the special factorial product by the current factorial.
    4. Return the final special factorial product."""
    
    # Step 1: Initialize the running product of the special factorial
    special_factorial_product = 1
    
    # Step 2: Initialize the current factorial
    current_factorial = 1
    
    # Step 3: Iterate from 1 to the input number (n)
    for i in range(1, n+1):
        # Calculate the factorial of the current number
        current_factorial *= i
        
        # Multiply the special factorial product by the current factorial
        special_factorial_product *= current_factorial
    
    # Step 4: Return the final special factorial product
    return special_factorial_product