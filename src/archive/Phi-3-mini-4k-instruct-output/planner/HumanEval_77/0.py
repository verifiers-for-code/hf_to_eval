def iscube(a):
    """
    This function takes an integer a and returns True if this integer is a cube of some integer number.
    
    Args:
    a (int): The input integer.
    
    Returns:
    bool: True if a is a cube of some integer number, False otherwise.
    
    Examples:
    >>> iscube(1)
    True
    >>> iscube(2)
    False
    >>> iscube(-1)
    True
    >>> iscube(64)
    True
    >>> iscube(0)
    True
    >>> iscube(180)
    False
    """
    # Check if the input is a cube of some integer number
    cube_root = round(a ** (1/3))
    return cube_root ** 3 == a