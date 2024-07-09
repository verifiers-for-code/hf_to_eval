from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    

    Action Plan:
    1. Initialize an empty list to store unique elements.
    2. Iterate through each element in the input list:
        a. Check if the current element is not already in the unique elements list.
        b. If the element is not a duplicate:
            - Add the element to the unique elements list.
    3. After iterating through the entire input list, return the unique elements list.
    4. Ensure the order of elements in the unique elements list is the same as in the input list.
    Note: Consider using a data structure that preserves the order of elements, such as a list or OrderedDict."""
    
    unique_elements = []
    for num in numbers:
        if num not in unique_elements:
            unique_elements.append(num)
    return unique_elements