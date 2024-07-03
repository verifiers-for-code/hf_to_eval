def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    Args:
    x (int): The start of the range.
    y (int): The end of the range.

    Returns:
    int: The biggest even number in the range [x, y] or -1 if no even number is found.

    Action Plan:
    1. Initialize a variable `max_even` to store the maximum even number, set it to -1 initially.
    2. Iterate through the range [x, y] using a loop.
    3. For each number in the range:
        a. Check if the number is even by using the modulus operator (%).
        b. If the number is even, compare it with `max_even`.
        c. If the number is greater than `max_even`, update `max_even` with the new number.
    4. After the loop, check if `max_even` is still -1.
    5. If `max_even` is -1, return -1, indicating no even number was found in the range.
    6. Otherwise, return `max_even`, which is the biggest even number in the range.
    
    Note: Use a loop to iterate through the range [x, y] efficiently.
    Be careful when checking for even numbers and updating the maximum even number.
    """
    max_even = -1
    for num in range(x, y + 1):
        if num % 2 == 0:
            if num > max_even:
                max_even = num
                
    return max_even