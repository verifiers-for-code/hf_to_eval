def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  
    Action Plan:
    1. Check if all input numbers (x, y, and z) are integers
       - Use a method to verify the type of each input
    
    2. If all inputs are integers:
       a. Check if x is equal to the sum of y and z
       b. Check if y is equal to the sum of x and z
       c. Check if z is equal to the sum of x and y
       - If any of these conditions are true, return True
    
    3. If the inputs are not all integers or none of the sum conditions are met:
       - Return False
    
    Note: Remember to handle negative integers as well, as shown in the examples.
    '''
    # Check if all inputs are integers
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        # Check if any of the sum conditions are met
        if x == y + z or y == x + z or z == x + y:
            return True
    return False