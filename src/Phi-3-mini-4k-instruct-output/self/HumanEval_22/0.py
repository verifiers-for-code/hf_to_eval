from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.
    
    Action Plan:
    1. Initialize an empty list to store filtered integers.
    
    2. Iterate over each element in the input list:
        a. Check the element's type to confirm if it's an integer.
    
    3. If the element is an integer, append it to the list of filtered integers.
    
    4. Optionally, handle mixed-type lists:
        a. Implement a separate function to identify all integer types (including negative integers).
        b. Apply this function to the list and return the filtered elements.
    
    5. Return the list of filtered integers.
    
    6. Write test cases to validate the function's correctness for various input scenarios, including mixed types.
    """
    filtered_integers = []
    for value in values:
        if isinstance(value, int):
            filtered_integers.append(value)
    return filtered_integers