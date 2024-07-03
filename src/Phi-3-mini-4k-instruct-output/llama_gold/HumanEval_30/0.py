def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    

    Action Plan:
    1. Initialize an empty list to store the positive numbers.
    2. Iterate through each element in the input list:
       a. Check if the element is greater than 0 (i.e., it's a positive number).
       b. If the element is positive, add it to the result list.
    3. Return the list containing only the positive numbers from the original list."""
    
    # Step 1: Initialize an empty list to store the positive numbers
    positive_numbers = []
    
    # Step 2: Iterate through each element in the input list
    for num in l:
        # Step 2a: Check if the element is greater than 0
        if num > 0:
            # Step 2b: If the element is positive, add it to the result list
            positive_numbers.append(num)
    
    # Step 3: Return the list containing only the positive numbers from the original list
    return positive_numbers