from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
    numbers (List[int]): The input list of integers
    delimeter (int): The number to be inserted between consecutive elements

    Returns:
    List[int]: A new list with the delimeter inserted between every two consecutive elements

    Examples:
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    # Step 1: Check if the input list `numbers` is empty
    if not numbers:
        return []

    # Step 2: Initialize an empty list `result` to store the interspersed elements
    result = []

    # Step 3: Iterate through the input list `numbers` with an index `i`
    for i in range(len(numbers)):
        # For each element at index `i`, add it to the `result` list
        result.append(numbers[i])

        # If `i` is not the last index, add the delimiter `delimeter` to the `result` list
        if i < len(numbers) - 1:
            result.append(delimeter)

    # Step 4: Return the `result` list
    return result