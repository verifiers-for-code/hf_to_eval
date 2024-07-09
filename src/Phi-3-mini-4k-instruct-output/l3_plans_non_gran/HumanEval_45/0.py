def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    
    Action Plan:
    1. Define a function `triangle_area` that takes two parameters: `a` and `h`, representing the length of a side and the height of a triangle, respectively.
    2. Inside the function, calculate the area of the triangle using the formula: `0.5 * a * h`.
    3. Return the calculated area as a float value.
    4. Test the function with example inputs, such as `a = 5` and `h = 3`, to ensure it produces the correct result (7.5).
    5. Document the function with a clear docstring, explaining the purpose, parameters, and return value."""
    
    # Calculate the area of the triangle
    area = 0.5 * a * h
    
    # Return the calculated area as a float value
    return float(area)