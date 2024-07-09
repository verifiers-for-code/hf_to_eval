def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    

    Action Plan:
    1. Convert the input integer `x` to a string to allow for easy manipulation of its digits.
    
    2. Calculate the number of digits in the string representation of `x`.
    
    3. Determine the actual shift amount by taking the remainder of `shift` divided by the number of digits.
    
    4. Implement the circular shift logic:
        a. If the shift amount is 0, return the original string.
        b. If the shift amount is greater than the number of digits, return the string with the digits reversed.
        c. Otherwise, extract the substring starting from the shift amount to the end of the string and concatenate it with the substring from the beginning of the string up to the shift amount.
    
    5. Return the resulting string.
    
    Note: Use appropriate string manipulation methods for slicing and concatenation.
    Be careful when handling the edge case where the shift amount is greater than the number of digits."""
    
    # Step 1: Convert the input integer `x` to a string
    x_str = str(x)
    
    # Step 2: Calculate the number of digits in the string representation of `x`
    num_digits = len(x_str)
    
    # Step 3: Determine the actual shift amount
    shift_amount = shift % num_digits
    
    # Step 4: Implement the circular shift logic
    if shift_amount == 0:
        # If the shift amount is 0, return the original string
        return x_str
    elif shift_amount > num_digits:
        # If the shift amount is greater than the number of digits, return the string with the digits reversed
        return x_str[::-1]
    else:
        # Otherwise, extract the substring starting from the shift amount to the end of the string and concatenate it with the substring from the beginning of the string up to the shift amount
        return x_str[shift_amount:] + x_str[:shift_amount]