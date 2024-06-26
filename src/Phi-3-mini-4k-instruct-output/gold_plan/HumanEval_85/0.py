def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices.

    Action Plan:
    1. Initialize a variable to store the sum of even elements.
    2. Iterate through the list starting from index 1 and stepping by 2 to access odd indices.
    3. For each element at an odd index:
       a. Check if the element is even (divisible by 2 with no remainder).
       b. If even, add it to the sum variable.
    4. After the iteration, return the final sum.

    Examples:
        add([4, 2, 6, 7]) ==> 2
    """
    # Step 1: Initialize a variable to store the sum of even elements
    sum_even_at_odd_indices = 0

    # Step 2: Iterate through the list starting from index 1 and stepping by 2 to access odd indices
    for i in range(1, len(lst), 2):
        # Step 3a: Check if the element is even
        if lst[i] % 2 == 0:
            # Step 3b: If even, add it to the sum variable
            sum_even_at_odd_indices += lst[i]

    # Step 4: Return the final sum
    return sum_even_at_odd_indices