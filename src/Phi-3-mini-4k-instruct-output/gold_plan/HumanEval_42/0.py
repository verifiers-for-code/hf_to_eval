def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
    Action Plan:
    1. Create a new list to store the incremented values.
    2. Iterate through each element in the input list 'l'.
    3. For each element:
       a. Add 1 to the element.
       b. Add the result to the new list.
    4. Use a list comprehension to perform steps 2-3 in a single line.
       - The list comprehension should:
         i. Iterate over each element 'e' in the input list 'l'
         ii. Apply the operation 'e + 1' to each element
         iii. Construct a new list with the results
    5. Return the new list containing the incremented values.
    """
    return [e + 1 for e in l]