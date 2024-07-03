def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    
    1. Understand the formula for the area of a triangle:
       - The area of a triangle is calculated as 0.5 * base * height
       - In this case, the base is the given side length 'a' and the height is the given 'h'
    
    2. Implement the formula using the given side length and height:
       - Multiply the side length 'a' by the height 'h'
       - Divide the result by 2 (since the area is 0.5 * base * height)
    
    3. Return the calculated area:
       - Assign the result of the calculation to a variable (e.g., 'area')
       - Return the 'area' variable as the result of the function
    
    Additional implementation details:
    - Ensure the function takes two parameters: 'a' (side length) and 'h' (height)
    - Use the correct data types for 'a' and 'h' (e.g., int or float)
    - Consider adding input validation to handle invalid input values (e.g., negative side lengths or heights)
    - Test the function with sample inputs to verify its correctness
    """
    # Input validation
    if a <= 0 or h <= 0:
        raise ValueError("Side length and height must be positive values")
    
    # Calculate the area
    area = 0.5 * a * h
    
    # Return the area
    return area