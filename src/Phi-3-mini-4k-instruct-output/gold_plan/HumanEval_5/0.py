from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    # Step 1: Check if the input list 'numbers' is empty. If so, return an empty list.
    if not numbers:
        return []

    # Step 2: Create an empty list to store the result.
    result = []

    # Step 3: Iterate through the elements of 'numbers', excluding the last element:
    for i in range(len(numbers) - 1):
        # a. Append the current element to the result list.
        result.append(numbers[i])
        # b. Append the 'delimeter' to the result list.
        result.append(delimeter)

    # Step 4: After the loop, append the last element of 'numbers' to the result list.
    result.append(numbers[-1])

    # Step 5: Return the result list.
    return result