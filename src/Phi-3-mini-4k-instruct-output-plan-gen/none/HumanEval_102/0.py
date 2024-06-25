
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # Check if x and y are positive
    if x <= 0 or y <= 0:
        return -1

    # Find the biggest even number in the range [x, y]
    biggest_even = -1
    for i in range(x, y + 1):
        if i % 2 == 0:
            biggest_even = i

    return biggest_even