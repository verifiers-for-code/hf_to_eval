def sum_squares(lst):
    """
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries.
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    

    Action Plan:
    1. Initialize a variable `sum_of_squares` to store the sum of the squared and cubed values, set it to 0.
    
    2. Iterate through the list using the `enumerate` function, which returns both the index and value of each element.
    
    3. Inside the loop, apply the following conditional logic:
        a. If the index is a multiple of 3, square the value and add it to `sum_of_squares`.
        b. If the index is a multiple of 4 and not a multiple of 3, cube the value and add it to `sum_of_squares`.
        c. If the index is not a multiple of 3 or 4, leave the value unchanged.
    
    4. Update the list in place by modifying the values based on the conditional logic.
    
    5. After the loop, return the final `sum_of_squares` value.
    
    Note: Be careful with the conditional logic and indexing to ensure correct implementation.
    """
    sum_of_squares = 0
    for i, val in enumerate(lst):
        if i % 3 == 0:
            sum_of_squares += val ** 2
        elif i % 4 == 0 and i % 3 != 0:
            sum_of_squares += val ** 3
    return sum_of_squares