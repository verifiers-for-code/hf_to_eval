def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    

    Action Plan:
    1. Check if x is greater than y. If true, return -1 as the range is invalid.
    2. Check if y is an even number. If true, return y as it's the largest even number in the range.
    3. Check if x is equal to y. If true, return -1 as there's no range to find an even number.
    4. Since y is not even, subtract 1 from y to find the largest even number in the range [x, y].
       a. If the result is greater than or equal to x, return this number.
       b. If the result is less than x, return -1 as no even number is found in the range."""

    # Step 1: Check if x is greater than y
    if x > y:
        return -1

    # Step 2: Check if y is an even number
    if y % 2 == 0:
        return y

    # Step 3: Check if x is equal to y
    if x == y:
        return -1

    # Step 4: Subtract 1 from y to find the largest even number in the range [x, y]
    largest_even = y - 1

    # Check if the result is greater than or equal to x
    if largest_even >= x:
        return largest_even

    # If the result is less than x, return -1
    return -1