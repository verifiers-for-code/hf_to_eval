def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    

    Action Plan:
    1. Function Purpose and Initial Setup:
        - Start with a list `l` that may contain duplicate elements
    
    2. Sort the List:
        - Use the list's sort method to order the elements from lowest to highest
    
    3. Extract Unique Elements:
        - Initialize an empty list to hold the unique elements
        - Iterate through the sorted list
            - If the current element is not in the unique list:
                - Append the element to the unique list
    
    4. Sort the Extracted Unique Elements:
        - Use the list's sort method again on the unique list to sort it from smallest to largest
    
    5. Considerations for Efficiency:
        - Sorting the list first helps to find duplicates in O(n log n) time complexity, which can be more efficient than other methods.
        - Using a set for uniqueness checks can be more time-efficient but might sacrifice the sorted order, so sorting the list is essential.
    
    6. Testing:
        - Verify the function with test cases like the provided example
        - Test with empty lists, lists with all duplicates, lists with various non-sequential numbers, and lists with negative numbers"""
    l.sort()
    unique_list = []
    for element in l:
        if element not in unique_list:
            unique_list.append(element)
    unique_list.sort()
    return unique_list