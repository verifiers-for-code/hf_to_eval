def car_race_collision(n: int) -> int:
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    
    Action Plan:
    1. Recognize that each car moving left to right will collide with every car moving right to left.
    2. Understand that the number of collisions is not affected by the cars' speed or their initial positions.
    3. Identify that the number of collisions is solely dependent on the number of cars 'n' in each direction.
    4. Derive the relationship: each of the 'n' cars moving left to right will collide with all 'n' cars moving right to left, resulting in 'n' x 'n' collisions.
    5. Express the solution as a function of 'n', which is simply the square of 'n'.
    
    Note: Think about how the number of collisions changes when you add one more car to each direction.
    """
    return n * n