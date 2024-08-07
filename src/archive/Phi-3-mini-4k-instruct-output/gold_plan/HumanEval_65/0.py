def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Step 1: Convert the integer x to a string
    x_str = str(x)
    
    # Step 2: Check if the shift value is greater than the length of the string
    if shift > len(x_str):
        # If true, reverse the string and return it
        return x_str[::-1]
    
    # Step 3: If shift is less than or equal to the string length, perform the circular shift
    else:
        # Extract the last 'shift' number of characters from the string
        last_part = x_str[-shift:]
        # Extract the remaining characters from the beginning of the string
        first_part = x_str[:-shift]
        # Concatenate the extracted parts in the new order (last part + first part)
        result = last_part + first_part
        
    # Step 4: Return the resulting string
    return result