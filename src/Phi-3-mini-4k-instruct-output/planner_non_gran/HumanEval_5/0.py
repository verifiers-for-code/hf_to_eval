from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    

    Action Plan:
    1. Check if the input list `numbers` is empty:
        - If it is, return an empty list
    
    2. Initialize an empty list `result` to store the interspersed elements
    
    3. Iterate through the input list `numbers` with an index `i`:
        - For each element at index `i`, add it to the `result` list
        - If `i` is not the last index, add the delimiter `delimeter` to the `result` list
    
    4. Return the `result` list, which now contains the interspersed elements
    
    Note: Use a loop to iterate through the input list and conditional statements to handle the insertion of the delimiter.
    Be careful to avoid inserting the delimiter at the end of the list."""
    
    if not numbers:
        return []
    
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimeter)
    
    return result