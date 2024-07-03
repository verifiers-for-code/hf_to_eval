def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    

    Action Plan:
    1. Initialize the function with two parameters: the list of numbers `l` and the threshold threshold `t`.
    
    2. Iterate over each element in the list using a loop:
        a. Check if the current element is greater than or equal to the threshold
    
    3. If any element is greater than or equal to the threshold, return False
    
    4. If the loop completes without finding any element greater than or equal to the threshold, return True
    
    5. Account for edge cases:
        a. An empty list
        b. A list where all elements are equal to the threshold"""
    
    # Check if the list is empty
    if not l:
        return True
    
    # Iterate over each element in the list
    for num in l:
        # Check if the current element is greater than or equal to the threshold
        if num >= t:
            return False
    
    # If the loop completes without finding any element greater than or equal to the threshold, return True
    return True