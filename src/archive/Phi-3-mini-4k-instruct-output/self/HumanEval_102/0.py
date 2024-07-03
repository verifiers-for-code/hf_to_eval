def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # Input validation
    if not (isinstance(x, int) and isinstance(y, int) and x > 0 and y > 0):
        return -1

    # Range check
    if x > y:
        return -1

    # Generate a list of even numbers within the range
    even_nums = [num for num in range(x, y+1) if num % 2 == 0]

    # Handling the absence of an even number
    if not even_nums:
        return -1

    # Finding the maximum even number
    return max(even_nums)