def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    # Check if the input is a non-negative integer
    if a < 0:
        return False
    
    # Find the cube root of the input
    cube_root = round(a ** (1/3))
    
    # Check if the cube of the cube root is equal to the input
    return cube_root ** 3 == a