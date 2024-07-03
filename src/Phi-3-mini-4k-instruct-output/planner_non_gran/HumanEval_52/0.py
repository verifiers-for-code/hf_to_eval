def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    

    Action Plan:
    1. Define the function `below_threshold` with two parameters: `l` (a list of numbers) and `t` (an integer threshold).
    2. Initialize a boolean variable `all_below_threshold` to `True` to track if all numbers are below the threshold.
    3. Iterate through each number `num` in the list `l`:
        a. Check if `num` is greater than or equal to the threshold `t`.
        b. If `num` is greater than or equal to `t`, set `all_below_threshold` to `False` and break the loop.
    4. After iterating through the entire list, return the value of `all_below_threshold`.
    5. If `all_below_threshold` is `True`, it means all numbers in the list are below the threshold; otherwise, it means at least one number is not below the threshold."""
    all_below_threshold = True
    for num in l:
        if num >= t:
            all_below_threshold = False
            break
    return all_below_threshold