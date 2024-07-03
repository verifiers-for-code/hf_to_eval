from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Parameters:
    values (List[Any]): A list containing any Python values.

    Returns:
    List[int]: A list containing only the integer values from the input list.

    Examples:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    # Initialize an empty list to store the filtered integers
    filtered_integers = []

    # Iterate over each value in the input list
    for value in values:
        # Check if the value is an instance of the int class (i.e., an integer)
        if isinstance(value, int):
            # If the value is an integer, add it to the filtered list
            filtered_integers.append(value)

    # Return the filtered list of integers
    return filtered_integers