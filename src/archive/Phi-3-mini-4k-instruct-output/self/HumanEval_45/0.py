def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    # Step 1: Implement the formula for the area of a triangle
    if a <= 0 or h <= 0:
        return None
    area = 0.5 * a * h
    
    # Step 2: Structure the function
    return area

# Step 3: Discuss edge cases
if a < 0:
    return "Invalid triangle: side length cannot be negative."
if h <= 0:
    return "Invalid triangle: height cannot be zero or negative."

# Step 4: Deciding on the return type