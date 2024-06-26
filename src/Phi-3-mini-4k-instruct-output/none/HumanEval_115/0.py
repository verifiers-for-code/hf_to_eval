def max_fill(grid, capacity):
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.
    """
    import math
    rows = len(grid)
    cols = len(grid[0])
    total_water = 0

    for row in grid:
        total_water += sum(row)

    bucket_count = math.ceil(total_water / capacity)

    return bucket_count