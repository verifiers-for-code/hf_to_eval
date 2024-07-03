def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    # Step 1: Define the function signature with x (integer) and base (base-10 number less than 10) parameters
    
    # Step 2: Initialize an empty string variable to store the result
    result = ""
    
    # Step 3: Handle edge cases
    if base > 10 or base < 2:
        return "Error: Base must be a number less than 10."
    if x == 0:
        return "0"
    
    # Step 4: Implement a while-loop that runs until x becomes 0
    while x > 0:
        # Inside the loop, calculate the remainder of x divided by base and append it to the result string
        remainder = x % base
        result += str(remainder)
        # Update x to be the quotient of x divided by base
        x = x // base
    
    # Step 5: Reverse the result string to get the correct base representation
    result = result[::-1]
    
    # Step 6: Return the result string
    return result