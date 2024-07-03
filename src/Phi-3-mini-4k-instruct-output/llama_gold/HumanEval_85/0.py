def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..

    Examples:
        add([4, 2, 6, 7]) ==> 2 

    Action Plan:
    1. Initialize a variable to store the sum of even elements at odd indices.
    2. Iterate through the input list, considering only odd indices (1, 3, 5, ...).
    3. For each element at an odd index:
       a. Check if the element is even (divisible by 2).
       b. If it's even, add the element to the sum variable.
    4. Return the final sum of even elements at odd indices."""

    # Step 1: Initialize a variable to store the sum of even elements at odd indices.
    sum_even_odd_indices = 0

    # Step 2: Iterate through the input list, considering only odd indices (1, 3, 5, ...).
    for i in range(1, len(lst), 2):
        # Step 3a: Check if the element is even (divisible by 2).
        if lst[i] % 2 == 0:
            # Step 3b: If it's even, add the element to the sum variable.
            sum_even_odd_indices += lst[i]

    # Step 4: Return the final sum of even elements at odd indices.
    return sum_even_odd_indices