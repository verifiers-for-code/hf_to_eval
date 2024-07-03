def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    
    Args:
    x (int): The input number.
    base (int): The desired base.
    
    Returns:
    str: The string representation of the input number x in the desired base.
    
    Raises:
    ValueError: If x or base is not an integer or if base is not less than 10.
    
    Examples:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise ValueError("Both x and base must be integers.")
    if base < 2 or base > 10:
        raise ValueError("Base must be less than 10.")
    
    result = ""
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x = x // base
    return result