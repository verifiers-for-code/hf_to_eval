def max_element(l: list):
    """Return maximum element in the list.

    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    # Step 1: Initialize a variable 'max_val' with the first element of the input list 'l'
    max_val = l[0]

    # Step 2: Iterate through each element 'e' in the list 'l'
    for e in l:
        # Step 2a: Compare 'e' with 'max_val'
        if e > max_val:
            # Step 2b: If 'e' is greater than 'max_val', update 'max_val' to be 'e'
            max_val = e

    # Step 3: After the iteration is complete, return 'max_val'
    return max_val