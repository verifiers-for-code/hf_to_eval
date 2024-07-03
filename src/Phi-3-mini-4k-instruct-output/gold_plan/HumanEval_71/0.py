import math

def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1

    Action Plan:
    1. Check if the triangle is valid:
       - Compare the sum of each pair of sides with the third side
       - If any sum is less than or equal to the third side, return -1

    2. If the triangle is valid, calculate the semi-perimeter:
       - Add all three sides and divide by 2

    3. Use Heron's formula to calculate the area:
       - Area = sqrt(s * (s-a) * (s-b) * (s-c))
       where s is the semi-perimeter

    4. Round the calculated area to 2 decimal places

    5. Return the rounded area
    '''
    # Check if the triangle is valid
    if a + b <= c or a + c <= b or b + c <= a:
        return -1

    # Calculate the semi-perimeter
    s = (a + b + c) / 2

    # Use Heron's formula to calculate the area
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    # Round the calculated area to 2 decimal places
    rounded_area = round(area, 2)

    # Return the rounded area
    return rounded_area