def below_threshold(l: list, t: int) -> bool:
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    # Step 1: Initialize the function with two parameters: the list of numbers `l` and the threshold `t`.
    if not l:  # Step 5: Account for edge case: An empty list
        return True

    for num in l:  # Step 2: Iterate over each element in the list using a loop
        if num >= t:  # Step 2a: Check if the current element is greater than or equal to the threshold
            return False  # Step 3: If any element is greater than or equal to the threshold, return False

    return True  # Step 4: If the loop completes without finding any element greater than or equal to the threshold, return True