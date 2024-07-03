def max_fill(grid, capacity):
    import math
    total_lowerings = 0
    for row in grid:
        total_water = sum(row)
        lowerings = math.ceil(total_water / capacity)
        total_lowerings += lowerings
    return total_lowerings