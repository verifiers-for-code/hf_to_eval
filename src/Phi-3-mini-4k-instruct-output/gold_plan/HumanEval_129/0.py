def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with you current
    cell.
    Please note that a path A (of length k) means visiting exactly k cells (not
    necessarily distinct).
    You CANNOT go off the grid.
    A path A (of length k) is considered less than a path B (of length k) if
    after making the ordered lists of the values on the cells that A and B go
    through (let's call them lst_A and lst_B), lst_A is lexicographically less
    than lst_B, in other words, there exist an integer index i (1 <= i <= k)
    such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have
    lst_A[j] = lst_B[j].
    It is guaranteed that the answer is unique.
    Return an ordered list of the values on the cells that the minimum path go through.

    Examples:

        Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
        Output: [1, 2, 1]

        Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
        Output: [1]

    Action Plan:
    1. Initialize variables:
       - n: size of the grid (number of rows/columns)
       - val: initialize with a value larger than any possible grid value

    2. Find the position of 1 in the grid:
       - Iterate through the grid
       - When 1 is found, check its neighbors:
         - For each valid neighbor (within grid bounds), add to a temporary list
         - Find the minimum value among these neighbors
         - Update 'val' with this minimum neighbor value

    3. Create the path:
       - Initialize an empty list 'ans' to store the path
       - Iterate k times:
         - For even indices (including 0), append 1 to 'ans'
         - For odd indices, append 'val' to 'ans'

    4. Return the constructed path 'ans'

    Note: This approach works because the minimum path will always alternate
    between 1 (the smallest value in the grid) and its smallest neighbor.
    """
    n = len(grid)
    val = float('inf')

    # Find the position of 1 in the grid
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                neighbors = []
                if i > 0:
                    neighbors.append(grid[i-1][j])
                if i < n-1:
                    neighbors.append(grid[i+1][j])
                if j > 0:
                    neighbors.append(grid[i][j-1])
                if j < n-1:
                    neighbors.append(grid[i][j+1])
                val = min(val, min(neighbors))

    # Create the path
    ans = []
    for i in range(k):
        if i % 2 == 0:
            ans.append(1)
        else:
            ans.append(val)

    return ans