def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    # Action Plan
    # 1. Check for a base case first:
    #    a. If the length of the input list is less than 2, return False (no distinct pair possible)
    if len(l) < 2:
        return False
    
    # 2. Create a set to hold numbers we've seen:
    seen = set()
    
    # Iterate through the list and for each number:
    for num in l:
        # Calculate its complement by negating the number (target = -num)
        target = -num
        
        # Check if the complement is in the set
        if target in seen:
            # If it is, return True (pair found)
            return True
        
        # If not, add the current number to the set
        seen.add(num)
    
    # After the loop ends, return False if no pair is found
    return False