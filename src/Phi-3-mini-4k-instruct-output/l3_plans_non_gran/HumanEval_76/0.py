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
    1. Define a function `is_simple_power` that takes two parameters: `x` and `n`.
    2. Check if `x` is an integer.
        - If not, return `False` immediately, as `x` cannot be a simple power of `n` if it's not an integer.
    3. Calculate the integer part of `x` raised to the power of `n` using the `**` operator.
    4. Compare the result with `x`.
        - If they are equal, return `True`, indicating that `x` is a simple power of `n`.
        - If they are not equal, return `False`, indicating that `x` is not a simple power of `n`.
    5. No need to handle edge cases, as the function will work correctly for all integer inputs.
    
    Note: The `**` operator will handle the calculation of `x` raised to the power of `n` correctly, including cases where `n` is 0 or 1."""
    if not isinstance(x, int):
        return False
    return x == n ** int(x ** (1 / n))