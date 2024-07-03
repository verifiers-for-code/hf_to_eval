def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5

    Action Plan:
    1. Understand the inputs:
       - 'a' represents the length of a side (base) of the triangle
       - 'h' represents the height (altitude) of the triangle
    
    2. Recall the formula for calculating the area of a triangle:
       - Area = (base * height) / 2
       - In this case, 'a' is the base and 'h' is the height
    
    3. Implement the calculation:
       - Multiply the two input parameters
       - Divide the result by 2
       - Consider using floating-point division for precise results
    
    4. Return the calculated area
    """
    area = (a * h) / 2
    return area