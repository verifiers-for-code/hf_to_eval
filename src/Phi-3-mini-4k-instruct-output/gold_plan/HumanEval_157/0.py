def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle, return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 90 degree.
    """
    # Step 2: Square each side length
    a_squared, b_squared, c_squared = a*a, b*b, c*c
    
    # Step 3: Check all three possible configurations of the triangle
    is_right_angled = (a_squared == b_squared + c_squared) or \
                      (b_squared == a_squared + c_squared) or \
                      (c_squared == a_squared + b_squared)
    
    # Step 5: Return the result of the boolean expression
    return is_right_angled