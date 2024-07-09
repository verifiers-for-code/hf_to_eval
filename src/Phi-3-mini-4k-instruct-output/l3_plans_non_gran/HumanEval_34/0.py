def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    

    Action Plan:
    1. Define the function unique that takes a list l as input.
    2. Convert the input list l to a set to remove duplicates. This will automatically remove any duplicate elements.
    3. Convert the set back to a list. This is necessary because sets are unordered, and we need to sort the list.
    4. Sort the list in ascending order. This can be done using the built-in sorted function.
    5. Return the sorted list. This will be the output of the unique function.
    
    Note: Consider using a set comprehension to create the set, and the sorted function to sort the list."""
    
    # Step 1: Define the function unique that takes a list l as input.
    def unique(l: list):
        # Step 2: Convert the input list l to a set to remove duplicates.
        unique_set = {x for x in l}
        # Step 3: Convert the set back to a list.
        unique_list = list(unique_set)
        # Step 4: Sort the list in ascending order.
        sorted_list = sorted(unique_list)
        # Step 5: Return the sorted list.
        return sorted_list