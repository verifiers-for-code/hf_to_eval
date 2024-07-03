def triangle_area(a, h):
    """
    Given length of a side and height, return the area of a triangle.
    
    Parameters:
    a (float): Length of a side of the triangle
    h (float): Height of the triangle
    
    Returns:
    float: Area of the triangle
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    area = 0.5 * a * h
    return area