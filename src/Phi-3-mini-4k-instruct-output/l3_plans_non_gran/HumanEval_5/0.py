from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`.
    
    Action Plan:
    1. Check if the input list `numbers` is empty:
        - If empty, return an empty list
    
    2. Initialize an empty list `result` to store the final result.
    
    3. Iterate through the indices of the input list `numbers`:
        - For each index `i`:
            a. Append the `i`-th element of `numbers` to `result`.
            b. Append the `delimeter` to `result`.
    
    4. After the iteration, return the `result` list.
    
    Note: Be careful when iterating through the indices and appending elements to the result list.
    Consider the edge case where the input list is empty.
    """
    if not numbers:
        return []
    
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i < len(numbers) - 1:
            result.append(delimeter)
    
    return result