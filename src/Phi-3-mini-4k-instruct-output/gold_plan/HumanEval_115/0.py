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
    1. Import the math module to use the ceil function.
    2. Create a list comprehension to process each row (well) in the grid:
       a. For each row, calculate the sum of water units (sum of 1s in the row).
       b. Divide the sum by the bucket capacity.
       c. Use math.ceil to round up the result to the nearest integer.
    3. Sum up all the rounded-up values from the list comprehension.
    4. Return the final sum, which represents the total number of bucket lowerings.

    Note: The list comprehension efficiently combines steps 2-4 into a single line of code.
    """
    return sum([math.ceil(sum(row)/capacity) for row in grid])