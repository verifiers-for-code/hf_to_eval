def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    '''
    # Step 1: Handle the input
    a = abs(a)
    
    # Step 2: Calculate the cube root
    cube_root = round(a**(1/3))
    
    # Step 3: Cube the rounded result
    cubed_result = cube_root ** 3
    
    # Step 4: Compare with the original input
    return cubed_result == a