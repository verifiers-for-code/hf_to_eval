def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False

    Action Plan:
    1. Initialize a loop to iterate through each element in the input list 'l'.
    2. For each element in the list:
       a. Check if the element is greater than or equal to the threshold 't'.
       b. If true, immediately return False as we've found an element not below the threshold.
    3. If the loop completes without returning False, it means all elements are below the threshold.
    4. Return True after the loop ends.
    
    Note: This plan ensures we check all elements efficiently and return the correct boolean result.
    """
    for num in l:
        if num >= t:
            return False
    return True