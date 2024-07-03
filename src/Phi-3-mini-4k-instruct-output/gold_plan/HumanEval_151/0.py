def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
    
    If the input list is empty, return 0.
    
    Action Plan:
    1. Initialize a variable to store the sum of squares, set it to 0.
    2. Iterate through each number in the input list:
       a. Check if the number is positive (greater than 0).
       b. Check if the number is an integer (no decimal point).
       c. Check if the number is odd (not divisible by 2).
       d. If all conditions are met:
          - Square the number.
          - Add the squared value to the sum.
    3. After the iteration, return the final sum.
    
    Note: Consider using a list comprehension with conditional filtering
    to achieve steps 2 and 3 in a concise manner.
    '''
    # Initialize the sum of squares to 0
    sum_of_squares = 0
    
    # Iterate through each number in the list
    for num in lst:
        # Check if the number is positive, an integer, and odd
        if num > 0 and num.is_integer() and num % 2 != 0:
            # Square the number and add it to the sum
            sum_of_squares += num ** 2
    
    # Return the final sum
    return sum_of_squares