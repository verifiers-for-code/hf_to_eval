def max_fill(grid, capacity):
    import math

    # Step 1: Calculate total water volume
    sum_of_water = sum(sum(row) for row in grid)

    # Step 2: Check for edge cases
    if sum_of_water == 0:
        return 0

    # Step 3: Compute the number of buckets needed
    buckets_needed = math.ceil(sum_of_water / capacity)

    return buckets_needed