def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle, return True if the three
    sides form a right-angled triangle, False otherwise.
    
    A right-angled triangle is a triangle in which one angle is right angle or 90 degree.
    
    Args:
    a (float): length of side a
    b (float): length of side b
    c (float): length of side c
    
    Returns:
    bool: True if the triangle is right-angled, False otherwise
    """
    # Sort the sides in ascending order
    sides = sorted([a, b, c])
    
    # Check if the triangle inequality holds
    if sides[0] + sides[1] <= sides[2]:
        return False
    
    # Check if the triangle is right-angled
    return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-6