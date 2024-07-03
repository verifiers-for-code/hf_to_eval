def sum_squares(lst):
    """
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries.
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    

    Action Plan:
    1. Initialize an empty list to store the modified elements.
    2. Iterate through the input list, keeping track of the index for each element:
       a. Check if the index is a multiple of 3:
          - If true, square the element and add it to the modified list.
       b. If the index is not a multiple of 3, check if it's a multiple of 4:
          - If true, cube the element and add it to the modified list.
       c. If the index is not a multiple of 3 or 4, add the original element to the modified list.
    3. Calculate the sum of the modified list.
    4. Return the final sum.
    """
    modified_lst = []
    for i, num in enumerate(lst):
        if i % 3 == 0:
            modified_lst.append(num ** 2)
        elif i % 4 == 0 and i % 3 != 0:
            modified_lst.append(num ** 3)
        else:
            modified_lst.append(num)
    return sum(modified_lst)