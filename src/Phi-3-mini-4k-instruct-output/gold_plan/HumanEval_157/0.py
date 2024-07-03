def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    
    Action Plan:
    1. Recall the Pythagorean theorem: In a right-angled triangle, the square of the length of the hypotenuse 
       (longest side) is equal to the sum of squares of the other two sides.
    2. Square each side length (a*a, b*b, c*c) to avoid floating-point precision issues.
    3. Check all three possible configurations of the triangle:
       a. Is 'a' the hypotenuse? Check if a*a == b*b + c*c
       b. Is 'b' the hypotenuse? Check if b*b == a*a + c*c
       c. Is 'c' the hypotenuse? Check if c*c == a*a + b*b
    4. If any of these conditions are true, the triangle is right-angled.
    5. Use the 'or' operator to combine these checks into a single boolean expression.
    6. Return the result of this boolean expression.
    '''
    # Step 2: Square each side length
    a_squared = a * a
    b_squared = b * b
    c_squared = c * c

    # Step 3: Check all three possible configurations of the triangle
    is_right_angle = (a_squared == b_squared + c_squared) or \
                     (b_squared == a_squared + c_squared) or \
                     (c_squared == a_squared + b_squared)

    # Step 6: Return the result of this boolean expression
    return is_right_angle