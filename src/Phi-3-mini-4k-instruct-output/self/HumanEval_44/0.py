def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    

    Action Plan:
    1. Define the function signature with x (integer) and base (base-10 number less than 10) parameters
    
    2. Initialize an empty string variable to store the result
    
    3. Handle edge cases:
        a. If base is greater than 10 or less than 2, return an error message
        b. If x is 0, return '0'
    
    4. Implement a while-loop that runs until x becomes 0
        a. Inside the loop, calculate the remainder of x divided by base and append it to the result string
        b. Update x to be the quotient of x divided by base
    
    5. Reverse the result string to get the correct base representation (since we've built it from least significant digit to most significant)
    
    6. Return the result string
    
    7. Optional: handle potential integer overflows if the base is too large (not necessary based on problem statement)"""
    
    # Step 3a: Handle edge cases
    if base < 2 or base > 10:
        return "Error: Base must be between 2 and 10."
    if x == 0:
        return '0'
    
    # Step 2: Initialize an empty string variable to store the result
    result = ''
    
    # Step 4: Implement a while-loop that runs until x becomes 0
    while x > 0:
        # Step 4a: Calculate the remainder of x divided by base and append it to the result string
        result += str(x % base)
        # Step 4b: Update x to be the quotient of x divided by base
        x //= base
    
    # Step 5: Reverse the result string to get the correct base representation
    result = result[::-1]
    
    # Step 6: Return the result string
    return result