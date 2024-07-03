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
    '''
    # Step 1: Check if all input numbers (x, y, and z) are integers
    if not all(isinstance(i, int) for i in [x, y, z]):
        return False

    # Step 2: Check if x is equal to the sum of y and z
    if x == y + z:
        return True
    # Step 2: Check if y is equal to the sum of x and z
    elif y == x + z:
        return True
    # Step 2: Check if z is equal to the sum of x and y
    elif z == x + y:
        return True
    else:
        return False