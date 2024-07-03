def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    
    1. Check if the input list is empty:
       - If the list is empty, return True (an empty list is considered monotonic)
    
    2. Initialize a flag to track if the list is monotonic:
       - Set the flag to True initially, assuming the list is monotonic
    
    3. Iterate through the list starting from the second element:
       - Use a loop to iterate over the indices of the list, starting from 1
    
    4. Compare each element with its previous element:
       - For each element, check if it is less than or greater than the previous element
       - If the comparison result is False, set the monotonic flag to False and break the loop
    
    5. Determine if the list is monotonic:
       - If the monotonic flag is still True after the loop, the list is monotonic
       - Return True to indicate that the list is monotonic
       - If the monotonic flag is False, the list is not monotonic
       - Return False to indicate that the list is not monotonic
    
    Additional implementation details:
    - Use a for loop to iterate over the indices of the list
    - Use indexing to access each element and its previous element
    - Use a conditional statement (if-else) to set the monotonic flag and break the loop
    - Return a boolean value (True or False) to indicate whether the list is monotonic or not"""
    if not l:
        return True
    is_monotonic = True
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            is_monotonic = False
            break
        elif l[i] > l[i-1]:
            is_monotonic = False
            break
    return is_monotonic