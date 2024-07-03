def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    

    Action Plan:
    1. Convert the input integer x to a string to easily access and manipulate its digits.
    2. Check if the shift value is greater than the number of digits in the string:
       a. If true, return the reversed string (since shift is equivalent to reversing the digits).
    3. If the shift value is not greater than the number of digits:
       a. Calculate the effective shift value by taking the modulus of shift with the number of digits (to handle cases where shift is greater than the number of digits).
       b. Split the string into two parts: the part to be shifted to the end and the part to remain at the beginning.
       c. Concatenate the two parts in the correct order to achieve the circular shift.
       d. Return the resulting string."""

    # Convert the input integer to a string
    x_str = str(x)

    # Check if the shift value is greater than the number of digits
    if shift > len(x_str):
        # If true, return the reversed string
        return x_str[::-1]

    # Calculate the effective shift value
    effective_shift = shift % len(x_str)

    # Split the string into two parts
    first_part = x_str[:-effective_shift]
    second_part = x_str[-effective_shift:]

    # Concatenate the two parts in the correct order
    result = second_part + first_part

    # Return the resulting string
    return result