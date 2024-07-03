def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    

    Action Plan:
    1. Check if n is 1. If so, return True if x is 1, and False otherwise.
    2. Initialize a variable to store the current power of n, starting with 1.
    3. Iterate through a loop, multiplying the current power by n, until the power is no longer less than x.
    4. Check if the final calculated power equals x. If it does, return True, indicating x is a simple power of n. Otherwise, return False."""
    
    # Step 1
    if n == 1:
        return x == 1
    
    # Step 2
    power = 1
    
    # Step 3
    while power < x:
        power *= n
    
    # Step 4
    return power == x