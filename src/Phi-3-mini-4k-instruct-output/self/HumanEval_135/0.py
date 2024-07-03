def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    

    Action Plan:
    1. Initialize a variable to store the index of the desired result. Set it to -1 initially.
    
    2. Iterate over the array using a loop, starting from the second element (index 1) since the first element has no preceding element:
        - Use a loop counter to access each element and its preceding element.
    
    3. Inside the loop, compare the current element with the element before it:
        - If the current element is not greater than or equal to the previous element,
    
    4. If such an element is found, update the result index to the current loop counter.
    
    5. After the loop completes, return the result index.
    
    6. Considerations:
        - Ensure the array does not have duplicate values.
        - Edge cases such as an empty array should be handled and return -1."""
    
    # Initialize the result index to -1
    result_index = -1
    
    # Iterate over the array starting from the second element
    for i in range(1, len(arr)):
        # Compare the current element with the previous one
        if arr[i] < arr[i-1]:
            # Update the result index if the current element is smaller
            result_index = i
    
    # Return the result index
    return result_index