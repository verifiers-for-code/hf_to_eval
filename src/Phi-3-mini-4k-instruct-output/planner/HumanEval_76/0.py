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
    1. Define the function `is_simple_power` with two parameters: `x` and `n`.
    2. Calculate `n` raised to the power of `int` using the `**` operator.
    3. Compare the result of the power calculation with `x`.
    4. If the result is equal to `x`, return `True`, indicating that `x` is a simple power of `n`.
    5. If the result is not equal to `x`, return `False`, indicating that `x` is not a simple power of `n`.
    6. Consider edge cases, such as `n` being 0 or 1, and handle them accordingly.
    
    Note: Use the `**` operator for exponentiation and the `int` function to convert the result to an integer.
    Be careful with the comparison operation to ensure accurate results."""
    if n == 0:
        return x == 0
    elif n == 1:
        return x == 1
    else:
        power = n ** int(x)
        return power == x