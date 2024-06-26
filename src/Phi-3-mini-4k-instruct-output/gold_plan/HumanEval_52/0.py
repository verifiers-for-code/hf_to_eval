def below_threshold(l: list, t: int) -> bool:
    """Return True if all numbers in the list l are below threshold t.

    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    # Step 1: Initialize a loop to iterate through each element in the input list 'l'
    for num in l:
        # Step 2a: Check if the element is greater than or equal to the threshold 't'
        if num >= t:
            # Step 2b: If true, immediately return False
            return False
    # Step 3: If the loop completes without returning False, it means all elements are below the threshold
    return True