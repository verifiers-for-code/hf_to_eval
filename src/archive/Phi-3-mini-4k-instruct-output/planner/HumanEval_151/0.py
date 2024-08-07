def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    Parameters:
    lst (list): A list of numbers
    
    Returns:
    int: The sum of squares of the numbers in the list that are odd, ignoring negative and non-integer numbers.
    
    Examples:
    >>> double_the_difference([1, 3, 2, 0])
    10
    >>> double_the_difference([-1, -2, 0])
    0
    >>> double_the_difference([9, -2])
    81
    >>> double_the_difference([0])
    0
    """
    result = 0
    for num in lst:
        if isinstance(num, int) and num > 0:
            if num % 2 != 0:
                result += num ** 2
    return result * 2