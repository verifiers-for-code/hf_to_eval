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
    1. Initialize variables to store the total water in the grid and the number of buckets needed.
    2. Iterate through each row in the grid:
        a. Calculate the total water in the current row by summing up the values in the row.
        b. Add the total water in the current row to the total water in the grid.
        c. Calculate the number of buckets needed by dividing the total water in the grid by the bucket capacity.
        d. If the number of buckets needed is not an integer, increment it by 1.
    3. Calculate the number of times to lower the buckets by subtracting 1 from the number of buckets needed.
    4. Return the number of times to lower the buckets.
    5. Consider edge cases, such as an empty grid or a grid with no water.
    
    Note: Use appropriate data structures and mathematical operations to efficiently solve the problem.
    Be careful when handling the division and rounding of the number of buckets needed.
    """
    total_water = 0
    num_buckets = 0
    for row in grid:
        row_water = sum(row)
        total_water += row_water
        num_buckets += math.ceil(row_water / capacity)
    return num_buckets - 1