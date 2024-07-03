def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    
    Action Plan:
    1. Implement the formula for the area of a triangle: Area = 0.5 * base * height
        a. Recognize that the provided side can serve as the base
        b. Use the provided height
        c. Validate that base and height are positive numbers
    
    2. Structure the function as follows:
        a. Accept arguments 'a' (the side) and 'h' (the height)
        b. Calculate the area using the provided formula
        c. Return the calculated area
    
    3. Discuss edge cases:
        a. If the height 'h' is zero or negative, the triangle does not exist, and an appropriate message should be returned
        b. If the provided side 'a' is negative, it represents an invalid triangle, and an appropriate message should be returned
    
    4. Deciding on the return type:
        a. Ensure the calculated area is a floating-point number to accommodate non-integer areas
        b. Return None or a similar indicator if the triangle can't exist (e.g., invalid inputs)
    
    5. Review and test the function with the given test case and additional scenarios to ensure correctness."""
    
    # Validate inputs
    if a <= 0 or h <= 0:
        return None
    
    # Calculate the area
    area = 0.5 * a * h
    
    return area