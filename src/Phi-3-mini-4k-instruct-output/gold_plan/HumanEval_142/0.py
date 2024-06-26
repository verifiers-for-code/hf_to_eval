def sum_squares(lst):
    """
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries.

    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126

    Action Plan:
    1. Initialize an empty list to store the modified values.
    2. Iterate through the input list using enumerate to access both index and value.
    3. For each item:
       a. If the index is divisible by 3 (use modulo operator), square the value.
       b. Else if the index is divisible by 4 (use modulo operator) and not by 3, cube the value.
       c. Else, keep the original value.
    4. Append the resulting value (modified or original) to the new list.
    5. After the loop, use the sum() function to calculate the sum of all values in the new list.
    6. Return the calculated sum.

    Note: Remember to handle the case of an empty input list, which should return 0.
    """
    modified_values = []
    for index, value in enumerate(lst):
        if index % 3 == 0:
            modified_values.append(value ** 2)
        elif index % 4 == 0 and index % 3 != 0:
            modified_values.append(value ** 3)
        else:
            modified_values.append(value)
    return sum(modified_values)