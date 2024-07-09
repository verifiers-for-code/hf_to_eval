from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    

    Action Plan:
    1. Define the function filter_integers with a parameter values, which is a list of any Python values.
    2. Initialize an empty list to store the filtered integers.
    3. Iterate over each value in the input list:
        a. Check if the value is an integer using the isinstance() function.
        b. If the value is an integer, add it to the filtered list.
    4. After iterating over all values, return the filtered list containing only the integers.
    5. Consider handling potential edge cases, such as an empty input list or non-list inputs.
    
    Note: Use the appropriate type checking and list manipulation techniques to implement the function correctly."""
    
    # Check if the input is a list
    if not isinstance(values, list):
        raise TypeError("Input must be a list")
    
    # Initialize an empty list to store the filtered integers
    filtered_integers = []
    
    # Iterate over each value in the input list
    for value in values:
        # Check if the value is an integer
        if isinstance(value, int):
            # Add the integer to the filtered list
            filtered_integers.append(value)
    
    # Return the filtered list containing only the integers
    return filtered_integers