def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    

    Action Plan:
    1. Define a function `get_positive` that takes a list `l` as input.
    2. Initialize an empty list `positive_numbers` to store the positive numbers.
    3. Iterate through each number `num` in the input list `l`:
        a. Check if `num` is greater than 0 (i.e., positive).
        b. If `num` is positive, add it to the `positive_numbers` list.
    4. After iterating through the entire list, return the `positive_numbers` list.
    5. Test the function with example inputs to ensure it works correctly.
    
    Note: Use a list comprehension or a for loop to iterate through the input list.
    Be careful when checking for positivity (greater than 0)."""
    positive_numbers = [num for num in l if num > 0]
    return positive_numbers