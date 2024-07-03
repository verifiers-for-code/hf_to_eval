import math

def triangle_area(a, b, c):
    """
    Given the lengths of the three sides of a triangle, return the area of the triangle rounded to 2 decimal points if the three sides form a valid triangle. Otherwise, return -1.
    
    A triangle is valid if the sum of any two sides is greater than the third side.
    
    Args:
    a (float): Length of the first side of the triangle
    b (float): Length of the second side of the triangle
    c (float): Length of the third side of the triangle
    
    Returns:
    float: The area of the triangle rounded to 2 decimal points if the triangle is valid, otherwise -1
    """
    # Check if the sides form a valid triangle
    if (a + b > c) and (a + c > b) and (b + c > a):
        # Calculate the semi-perimeter
        s = (a + b + c) / 2
        # Calculate the area using Heron's formula
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return round(area, 2)
    else:
        return -1