def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1

    Action Plan:
    1. Check if x is greater than y. If so, return -1 as there's no valid range.
    2. Check if y is even. If so, return y as it's the largest even number in the range.
    3. Check if x equals y. If so, return -1 as there's no even number (since y is odd from step 2).
    4. If we've reached this point, y is odd and x < y. Return y - 1, which is the largest even number in the range.
    """
    if x > y:
        return -1
    elif y % 2 == 0:
        return y
    elif x == y:
        return -1
    else:
        return y - 1