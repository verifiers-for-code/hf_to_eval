def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    

    Action Plan:
    1. Recall the formula for the area of a triangle: (base * height) / 2.
    2. Identify the given parameters: side length (a) and height (h).
    3. Apply the formula by multiplying the side length (a) and height (h), then divide the result by 2.
    4. Return the calculated area value."""
    area = (a * h) / 2
    return area