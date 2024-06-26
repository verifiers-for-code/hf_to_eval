from typing import List

def common(l1: List[int], l2: List[int]) -> List[int]:
    """Return sorted unique common elements for two lists.

    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    # Step 1: Initialize an empty set to store common elements
    common_elements = set()

    # Step 2: Iterate through each element in the first list (l1)
    for element in l1:
        # Step 3: Check if the element exists in the second list (l2)
        if element in l2:
            # Step 4: Add the element to the set
            common_elements.add(element)

    # Step 5: Convert the set to a list of unique elements
    common_elements = list(common_elements)

    # Step 6: Sort the list of common elements in ascending order
    common_elements.sort()

    # Step 7: Return the sorted list of common elements
    return common_elements