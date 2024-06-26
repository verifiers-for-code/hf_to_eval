def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    Parameters:
    lst (list): A list of numbers
    
    Returns:
    int: The sum of squares of the numbers in the list that are odd.
    """
    # Step 1: Initialize a variable to store the sum of squares, set it to 0.
    sum_of_squares = 0
    
    # Step 2: Iterate through each number in the input list.
    # Use a list comprehension with conditional filtering to achieve steps 2 and 3 in a concise manner.
    sum_of_squares += sum(x**2 for x in lst if x > 0 and isinstance(x, int) and x % 2 != 0)
    
    # Step 3: After the iteration, return the final sum.
    return sum_of_squares