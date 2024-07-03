def has_even_digits(num):
    """Helper function to check if a number has even digits.
    
    Args:
    num (int): The number to check.
    
    Returns:
    bool: True if the number has even digits, False otherwise.
    """
    # Iterate through each digit of the number
    for digit in str(num):
        # Check if the digit is even using the modulo operator
        if int(digit) % 2 == 0:
            return True
    return False

def unique_digits(x):
    """Given a list of positive integers x, return a sorted list of all elements that
    haven't any even digit.

    Args:
    x (list): A list of positive integers.

    Returns:
    list: A sorted list of positive integers without any even digits.

    Example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    # Use list comprehension to apply the helper function to each number in the input list
    # Filter numbers without any even digits
    filtered_list = [num for num in x if not has_even_digits(num)]
    
    # Sort the filtered list
    filtered_list.sort()
    
    return filtered_list