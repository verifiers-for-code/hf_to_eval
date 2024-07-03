def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.
    
    Action Plan:
    1. Utilize built-in set data structure for its efficiency in removing duplicates and finding intersections
    2. Convert lists to sets
    3. Perform intersection to find common elements
    4. Convert intersection set to a list
    5. Sort the list of common elements
    
    6. Edge cases:
        a. Handle empty lists
        b. Assess the impact of input lists having no common elements
        c. Check for cases where one list is a subset of the other
    
    7. Efficiency considerations:
        a. Use set operations for their inherent efficiency
        b. Maintain readable and maintainable code structure
    
    8. Testing:
        a. Confirm the function works with the provided test cases and additional edge cases
        b. Validate the output list is sorted as expected
    """
    # Handle empty lists
    if not l1 or not l2:
        return []
    
    # Convert lists to sets
    set1, set2 = set(l1), set(l2)
    
    # Perform intersection to find common elements
    common_elements = set1.intersection(set2)
    
    # Convert intersection set to a list and sort it
    sorted_common_elements = sorted(list(common_elements))
    
    return sorted_common_elements