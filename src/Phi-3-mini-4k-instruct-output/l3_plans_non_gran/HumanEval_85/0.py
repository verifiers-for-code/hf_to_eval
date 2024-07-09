def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2

    Action Plan:
    1. Initialize a variable (e.g., total) to store the sum of even numbers at odd indices, set it to 0.
    2. Iterate through the list using a for loop with a range that starts from 1 (for the second element) and increments by 2 (to access every second element).
    3. Within the loop, check if the current element at the odd index is even (i.e., lst[i] % 2 == 0).
    4. If the element is even, add it to the total variable.
    5. After the loop, return the total variable, which now holds the sum of even numbers at odd indices.
    Note: Pay attention to the indexing pattern to access every second element in the list.
    Use the modulo operator (%) to check if a number is even."""

    total = 0
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            total += lst[i]
    return total