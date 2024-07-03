def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
    Action Plan:
    1. Initialize a variable 'max_val' with the first element of the input list 'l'.
    2. Iterate through each element 'e' in the list 'l':
        a. Compare 'e' with 'max_val'.
        b. If 'e' is greater than 'max_val', update 'max_val' to be 'e'.
    3. After the iteration is complete, return 'max_val'.
    
    Note: This approach assumes the list is non-empty. For empty lists, consider
    adding appropriate error handling.
    """
    if not l:
        raise ValueError("Input list is empty")
    
    max_val = l[0]
    for e in l:
        if e > max_val:
            max_val = e
    return max_val