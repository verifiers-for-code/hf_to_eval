def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    

    Action Plan:
    1. Define the function `triangle_area` with two parameters: `a` (length of a side) and `h` (height)
    2. Calculate the area of the triangle using the formula: `area = 0.5 * a * h`
    3. Return the calculated area as a float value
    4. No need for error handling as the formula is valid for all positive values of `a` and `h`
    5. No need for input validation as the function assumes valid inputs"""
    area = 0.5 * a * h
    return float(area)