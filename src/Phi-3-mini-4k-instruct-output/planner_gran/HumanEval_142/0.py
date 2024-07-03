def sum_squares(lst):
    """
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries.
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    

    1. Initialize a variable to store the sum of the modified entries
       - Set the initial value to 0
    
    2. Iterate over the input list using enumerate() to access both the index and value of each element
       - Use a for loop to iterate over the list
    
    3. For each element, check the index:
       a. If the index is a multiple of 3 (using the modulo operator):
          - Square the element (use the exponentiation operator **)
       b. If the index is a multiple of 4 (using the modulo operator):
          - Cube the element (use the exponentiation operator **)
       c. If the index is neither a multiple of 3 nor 4:
          - Leave the element unchanged
    
    4. Add the modified element (or the original element if unchanged) to the sum variable
       - Use the += operator to add the value to the sum
    
    5. After iterating over all elements, return the final sum
       - Use the return statement to output the sum
    
    Additional implementation details:
    - Use the enumerate() function to iterate over the list with indexing
    - Use the modulo operator (%) to check for multiples of 3 and 4
    - Use the exponentiation operator (**) to square or cube the elements
    - Use the += operator to add the modified elements to the sum
    - Ensure that the function handles empty input lists correctly (return 0)"""
    
    sum_of_modified_entries = 0
    for index, value in enumerate(lst):
        if index % 3 == 0:
            sum_of_modified_entries += value ** 2
        elif index % 4 == 0 and index % 3 != 0:
            sum_of_modified_entries += value ** 3
        else:
            sum_of_modified_entries += value
    return sum_of_modified_entries