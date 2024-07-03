from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]

    Action Plan:
    1. Check if the input list 'numbers' is empty. If so, return an empty list.
    2. Create an empty list to store the result.
    3. Iterate through the elements of 'numbers', excluding the last element:
       a. Append the current element to the result list.
       b. Append the 'delimeter' to the result list.
    4. After the loop, append the last element of 'numbers' to the result list.
    5. Return the result list.
    """
    if not numbers:
        return []

    result = []
    for num in numbers[:-1]:
        result.append(num)
        result.append(delimeter)

    result.append(numbers[-1])
    return result