def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false

    Action Plan:
    1. Handle the special case where n is 1:
       - If n is 1, x can only be a simple power of n if x is also 1.
       - Return True if both n and x are 1, False otherwise.

    2. For all other cases, implement the following logic:
       - Start with a variable (let's call it 'power') initialized to 1.
       - While 'power' is less than x:
         * Multiply 'power' by n in each iteration.
         * This simulates calculating n^1, n^2, n^3, and so on.

    3. After the loop ends, compare 'power' with x:
       - If they are equal, x is a simple power of n, so return True.
       - If they are not equal, x is not a simple power of n, so return False.

    4. Ensure your implementation handles both positive and negative inputs for x and n correctly.

    By following these steps, you'll create a function that correctly determines
    if x is a simple power of n for all input cases.
    """
    if n == 1:
        return x == 1
    power = 1
    while power < x:
        power *= n
    return power == x