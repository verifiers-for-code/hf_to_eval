def max_fill(grid, capacity):
    import math
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    

    Action Plan:
    1. Parse the input grid and calculate its dimensions (rows and columns).
    2. Calculate the total water available in the grid by summing up the values in each row.
    3. Initialize a variable to count the number of times the bucket needs to be lowered.
    4. Implement a loop that continues until the bucket is filled or there's no more water in the grid:
        a. Find the column with the maximum water content in the current row.
        b. Calculate the amount of water that can be extracted from the column.
        c. Update the grid by subtracting the extracted water from the column.
        d. Increment the bucket fill count by the extracted water amount.
        e. Check if the bucket is filled (bucket capacity reached).
        f. If the bucket is filled, break the loop.
    5. Return the total count of times the bucket needs to be lowered."""

    rows = len(grid)
    cols = len(grid[0])
    total_water = sum(sum(row) for row in grid)
    bucket_fill_count = 0

    while total_water > 0:
        max_water_col = max(range(cols), key=lambda col: sum(grid[row][col] for row in range(rows)))
        water_to_extract = min(total_water, capacity)
        bucket_fill_count += water_to_extract
        total_water -= water_to_extract

        for row in range(rows):
            grid[row][max_water_col] -= water_to_extract

        if total_water == 0:
            break

    return bucket_fill_count