def max_fill(grid, capacity):
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
    1. Calculate total water volume:
        a. Initialize sum_of_water to 0
        b. Iterate through each row in the grid, summing up units of water
    
    2. Check for edge cases:
        a. Return 0 for an empty grid
        b. Return 0 for a grid with all zeros
    
    3. Compute the number of buckets needed:
        a. Divide the total water volume by the bucket capacity and round up (because you can't have a fraction of a bucket)
    
    4. Return the result as the number of buckets required"""

    import math

    # Step 1: Calculate total water volume
    sum_of_water = 0
    for row in grid:
        sum_of_water += sum(row)

    # Step 2: Check for edge cases
    if sum_of_water == 0:
        return 0

    # Step 3: Compute the number of buckets needed
    num_buckets = math.ceil(sum_of_water / capacity)

    # Step 4: Return the result
    return num_buckets