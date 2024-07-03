def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """
    # Step 1: Initialize a count for collisions and set of cars moving from each set
    collision_count = 0
    left_cars = list(range(n))
    right_cars = list(range(n, 2*n))

    # Step 2 & 3: Create a loop for the cars moving from the left set, tracking their current position
    # and for the cars moving from the right set, tracking their current position
    for left_car in left_cars:
        for right_car in right_cars:
            # Step 4: For each pair of cars, check if they are close enough to collide
            if abs(left_car - right_car) == 1:
                collision_count += 1
                # Step 5: Increment the collision count if a collision occurs

    # Step 6: Optimize the process by tracking only nearby cars and skipping pairs that can't collide
    # Since all cars move at the same speed and are infinitely sturdy, we only need to check for collisions
    # between adjacent cars in both sets.

    # Step 7: Output the final count of collisions
    return collision_count