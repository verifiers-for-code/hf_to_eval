def max_fill(grid, capacity):
    import math
    # Step 2: Create a list comprehension to process each row (well) in the grid
    bucket_lowerings = [math.ceil(sum(row) / capacity) for row in grid]
    # Step 3: Sum up all the rounded-up values from the list comprehension
    total_lowerings = sum(bucket_lowerings)
    # Step 4: Return the final sum
    return total_lowerings