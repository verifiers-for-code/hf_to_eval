def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    

    Action Plan:
    1. Define a function named max_element that takes a list l as input.
    2. Inside the function, use the built-in max() function to find the maximum element in the list l.
    3. The max() function will return the largest item in the list, which is the maximum element.
    4. Return the result of the max() function, which is the maximum element in the list.
    
    Note: The max() function is a built-in Python function that returns the largest item in an iterable or the largest of two or more arguments."""
    return max(l)