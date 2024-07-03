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

    Action Plan:
    1. Handle the input:
       - Consider using the absolute value of 'a' to handle both positive and negative inputs.
    
    2. Calculate the cube root:
       - Use exponentiation to find the approximate cube root of the absolute value of 'a'.
       - Hint: x^(1/3) is the cube root of x.
    
    3. Round the result:
       - Round the calculated cube root to the nearest integer.
       - Hint: Use a built-in function to round the result.
    
    4. Cube the rounded result:
       - Take the rounded value from step 3 and cube it.
    
    5. Compare with the original input:
       - Check if the result from step 4 is equal to the absolute value of the original input 'a'.
    
    6. Return the result:
       - Return True if the comparison in step 5 is true, otherwise return False.

    Note: Be careful with floating-point precision when performing these calculations.
    '''
    # Step 1: Handle the input
    a = abs(a)
    
    # Step 2: Calculate the cube root
    cube_root = a ** (1/3)
    
    # Step 3: Round the result
    rounded_cube_root = round(cube_root)
    
    # Step 4: Cube the rounded result
    cubed_rounded_cube_root = rounded_cube_root ** 3
    
    # Step 5: Compare with the original input
    if cubed_rounded_cube_root == a:
        return True
    else:
        return False