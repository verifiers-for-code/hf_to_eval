def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    

    Action Plan:
    1. Initialize a flag or variable to track the result (e.g., assume all elements are below the threshold).
    2. Iterate through each element in the input list:
       a. Compare the current element with the given threshold.
       b. If the element is greater than or equal to the threshold:
          - Immediately return False, indicating that not all elements are below the threshold.
    3. If the iteration completes without finding any elements above the threshold:
       a. Return True, indicating that all elements in the list are below the threshold."""
    
    # Step 1: Initialize a flag to track the result
    all_below_threshold = True
    
    # Step 2: Iterate through each element in the input list
    for num in l:
        # Step 2a: Compare the current element with the given threshold
        if num >= t:
            # Step 2b: If the element is greater than or equal to the threshold, return False
            all_below_threshold = False
            break  # Exit the loop as we found an element above the threshold
    
    # Step 3: If the iteration completes without finding any elements above the threshold, return True
    return all_below_threshold