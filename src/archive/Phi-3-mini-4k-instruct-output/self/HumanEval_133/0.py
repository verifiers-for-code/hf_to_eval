def sum_squares(lst):
    # Step 1: Round each number in the list to the nearest integer using the `int()` function applied to the ceiling value.
    rounded_lst = [int(math.ceil(x)) for x in lst]
    
    # Step 2 & 3: Create a list of squared numbers and sum them up using a single list comprehension statement.
    result = sum([x**2 for x in rounded_lst])
    
    # Step 4: Consider edge cases
    # a. Empty input list
    if not lst:
        return 0
    
    # b. List with all negative numbers
    if all(x < 0 for x in lst):
        return sum([x**2 for x in rounded_lst])
    
    # c. List with non-integer values
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("List must contain only integers or floats.")
    
    return result