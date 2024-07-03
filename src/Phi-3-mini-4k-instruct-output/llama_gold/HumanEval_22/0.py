from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    

    Action Plan:
    1. Initialize an empty list to store the filtered integer values.
    2. Iterate through each element in the input list:
       a. Check the type of the current element using a type checking function.
       b. If the element is an integer, add it to the filtered list.
    3. Return the filtered list containing only the integer values from the original list."""

    filtered_integers = []
    for value in values:
        if isinstance(value, int):
            filtered_integers.append(value)
    return filtered_integers