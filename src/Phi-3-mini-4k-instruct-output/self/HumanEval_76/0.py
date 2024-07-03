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
    1. Determine the core logic for checking if x is a simple power of n:
        - Use a loop to apply n**int and decrement the exponent
    
    2. Implement the core logic with an efficient and clear approach:
        - Initialize an exponent variable to 0
        - Begin a while loop, continuing until n**exponent either equals x or reaches a limit (e.g., when the number becomes too large)
        - Increment the exponent within the loop
    
    3. Handle edge cases:
        - If x is 1, return True
        - If n is 0, return False (since the power function is undefined)
        - If the loop ends without finding an integer exponent that makes n**exponent equal to x, return False
    
    4. Testing and validation:
        - Confirm the function returns expected results for a variety of test cases including simple powers, non-powers, and edge cases
    
    5. Optimize and refine:
        - Ensure that the loop has an appropriate stopping condition and that it can handle potential integer overflows or limits for n.
        - Use descriptive variable names and include comments for clarity."""

    # Handle edge cases
    if x == 1:
        return True
    if n == 0:
        return False

    exponent = 0
    while True:
        # Check if n raised to the current exponent equals x
        if n ** exponent == x:
            return True
        # Check if n raised to the current exponent is greater than x
        elif n ** exponent > x:
            return False