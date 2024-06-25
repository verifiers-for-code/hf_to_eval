def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    # Create a set to store the elements
    seen = set()
    
    # Iterate through the list
    for num in l:
        # Check if the negative of the current number is in the set
        if -num in seen:
            return True
        # Add the current number to the set
        seen.add(num)
    
    # If no pair is found, return False
    return False