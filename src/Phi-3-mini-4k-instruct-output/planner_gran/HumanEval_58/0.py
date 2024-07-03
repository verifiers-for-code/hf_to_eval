def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    

    1. Initialize an empty set to store the common elements:
       - Use a set to automatically remove duplicates
    
    2. Iterate through each element in the first list (l1):
       - Check if the current element is present in the second list (l2)
       - If it is, add the element to the set of common elements
    
    3. Iterate through each element in the second list (l2):
       - Check if the current element is present in the first list (l1)
       - If it is, add the element to the set of common elements
    
    4. Convert the set of common elements to a sorted list:
       - Use the sorted() function to sort the list in ascending order
    
    5. Return the sorted list of common elements:
       - The function should return a list of unique common elements, sorted in ascending order
    
    Additional implementation details:
    - Use a set to automatically remove duplicates from the common elements
    - Use the in operator to check if an element is present in a list
    - Use the sorted() function to sort the list in ascending order
    - Consider handling edge cases, such as empty input lists or lists with duplicate elements"""
    common_elements = set()
    for element in l1:
        if element in l2:
            common_elements.add(element)
    for element in l2:
        if element in l1:
            common_elements.add(element)
    return sorted(list(common_elements))