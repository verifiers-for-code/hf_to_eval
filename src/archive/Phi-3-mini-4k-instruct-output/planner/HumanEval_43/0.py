def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Action Plan:
    1. Initialize an empty set to store unique elements from the input list.
    2. Iterate through each element in the input list:
        a. Check if the negative of the current element is already in the set.
        b. If it is, return True, as we've found two distinct elements that sum to zero.
    3. If no such pair is found after iterating through the entire list, return False.
    4. Consider handling duplicates in the input list to ensure correctness.
    
    Note: Use a set to store unique elements for efficient lookups.
    Be careful to handle duplicates correctly to avoid false positives.
    """
    seen = set()
    for num in l:
        if -num in seen:
            return True
        seen.add(num)
    return False