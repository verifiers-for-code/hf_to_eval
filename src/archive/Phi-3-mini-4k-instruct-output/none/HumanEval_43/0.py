def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    # Create a set to store the elements of the list
    seen = set()
    
    # Iterate through the list
    for num in l:
        # Check if the negative of the current element is in the set
        if -num in seen:
            return True
        # Add the current element to the set
        seen.add(num)
    
    # If no pair is found, return False
    return False