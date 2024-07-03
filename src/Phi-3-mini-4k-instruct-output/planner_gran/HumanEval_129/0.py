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
    """
    n = len(grid)
    memo = [[-1 for _ in range(n)] for _ in range(n)]

    def helper(i, j, k):
        if k == 0:
            return 0
        if i < 0 or i >= n or j < 0 or j >= n:
            return float('inf')
        if memo[i][j] != -1:
            return memo[i][j]

        min_path = float('inf')
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < n and 0 <= y < n:
                path_len = helper(x, y, k-1)
                if path_len != float('inf'):
                    min_path = min(min_path, path_len + grid[i][j])

        memo[i][j] = min_path
        return min_path

    min_path_len = float('inf')
    for i in range(n):
        for j in range(n):
            path_len = helper(i, j, k)
            if path_len != float('inf'):
                min_path_len = min(min_path_len, path_len)

    if min_path_len == float('inf'):
        return []

    min_path = []
    for i in range(n):
        for j in range(n):
            if helper(i, j, k) == min_path_len:
                min_path.append(grid[i][j])
                break

    return min_path