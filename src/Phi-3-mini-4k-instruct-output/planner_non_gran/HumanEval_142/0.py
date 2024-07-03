def sum_squares(lst):
    """
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries.
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    

    Action Plan:
    1. Initialize a variable `total` to 0, which will store the sum of modified entries.
    2. Iterate through the input list `lst` using the `enumerate` function to get both the index and value of each element.
    3. For each element, check the following conditions:
        a. If the index is a multiple of 3 (i.e., `index % 3 == 0`), square the value and add it to `total`.
        b. If the index is a multiple of 4 (i.e., `index % 4 == 0`) and not a multiple of 3 (i.e., `index % 3!= 0`), cube the value and add it to `total`.
        c. If none of the above conditions are met, add the original value to `total`.
    4. After iterating through the entire list, return the final value of `total`.
    
    Note: Use the modulo operator (`%`) to check for multiples of 3 and 4.
    Be careful to handle the condition where the index is a multiple of 4 but not a multiple of 3 correctly.
    """
    total = 0
    for index, value in enumerate(lst):
        if index % 3 == 0:
            total += value ** 2
        elif index % 4 == 0 and index % 3 != 0:
            total += value ** 3
        else:
            total += value
    return total