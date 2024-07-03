from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    # Check if the input list `numbers` is empty. If so, return an empty list.
    if not numbers:
        return []
    
    # Initialize an empty list `result` to store the interspersed elements.
    result = []
    
    # Iterate through each element in the input list, excluding the last element:
    for i in range(len(numbers) - 1):
        # Append the current element to the `result` list.
        result.append(numbers[i])
        # Append the `delimiter` to the `result` list.
        result.append(delimeter)
    
    # Append the last element of the input list to the `result` list.
    result.append(numbers[-1])
    
    # Return the `result` list containing the interspersed elements.
    return result