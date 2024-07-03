def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Step 1: Normalize the shift value
    shift = shift % len(str(abs(x)))
    
    # Step 2: Convert the integer x into a string representation
    x_str = str(x)
    
    # Handle negative numbers
    if x < 0:
        x_str = '-' + x_str
    
    # Step 3: Manipulate the string
    if shift == 0:
        return x_str
    
    shifted_str = x_str[-shift:] + x_str[:-shift]
    
    # Step 4: Edge cases
    if shift >= len(x_str):
        return shifted_str[::-1]
    
    return shifted_str