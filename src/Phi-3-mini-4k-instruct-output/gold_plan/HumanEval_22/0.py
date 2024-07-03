from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]

    Action Plan:
    1. Initialize an empty list to store the filtered integers.
    2. Iterate through each element in the input 'values' list.
    3. For each element, check if it's an integer using the appropriate Python function.
    4. If the element is an integer, add it to the filtered list.
    5. After checking all elements, return the filtered list containing only integers.

    Hint: Look into list comprehension for a concise implementation.
    """
    return [value for value in values if isinstance(value, int)]