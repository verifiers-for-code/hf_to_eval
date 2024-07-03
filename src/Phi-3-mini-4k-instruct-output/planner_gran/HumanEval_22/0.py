from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    

    1. Understand the input list:
       - The function takes a list of any Python values as input
       - The list can contain integers, floats, strings, dictionaries, lists, etc.
    
    2. Initialize an empty list to store the filtered integers:
       - Create a new list that will hold the filtered integer values
    
    3. Iterate through each element in the input list:
       - Use a loop or list comprehension to process each element
       - Check if the current element is an integer using the isinstance() function
       - If the element is an integer, add it to the filtered list
    
    4. Return the filtered list of integers:
       - Once all elements have been processed, return the list of filtered integers
    
    Alternative approach using list comprehension:
    1. Initialize an empty list to store the filtered integers
    2. Use a list comprehension to iterate through the input list
    3. In the list comprehension, use isinstance() to check if each element is an integer
    4. If the element is an integer, add it to the filtered list
    5. Return the filtered list of integers
    
    Note: The function should handle empty input lists and lists containing a mix of different types (int, float, str, etc.) correctly."""
    filtered_integers = [value for value in values if isinstance(value, int)]
    return filtered_integers