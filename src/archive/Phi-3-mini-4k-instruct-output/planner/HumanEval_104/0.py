def has_even_digit(num):
    """Check if a number has any even digit.
    
    Args:
    num (int): The number to check.
    
    Returns:
    bool: True if the number has an even digit, False otherwise.
    """
    # Convert the number to a string to iterate over its digits
    for digit in str(num):
        # Check if the digit is even (using the modulus operator)
        if int(digit) % 2 == 0:
            return True
    return False

def unique_digits(x):
    """Return a sorted list of all elements in the input list that don't have any even digits.
    
    Args:
    x (list): A list of positive integers.
    
    Returns:
    list: A sorted list of numbers without even digits.
    
    Examples:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    # Initialize an empty list to store numbers without even digits
    result = []
    
    # Iterate over each number in the input list
    for num in x:
        # Check if the number has no even digits
        if not has_even_digit(num):
            # Add the number to the result list
            result.append(num)
    
    # Sort the result list in increasing order
    result.sort()
    
    return result