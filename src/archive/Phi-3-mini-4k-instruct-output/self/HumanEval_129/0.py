def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with you current
    cell.
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
    # Step 1: Validate input
    n = len(grid)
    if n < 2:
        raise ValueError("Grid must have at least 2 rows and columns.")
    if not all(len(row) == n for row in grid):
        raise ValueError("Grid must be a square matrix.")
    if not all(1 <= val <= n * n for row in grid for val in row):
        raise ValueError("Each cell must contain a unique value between 1 and N * N.")

    # Step 2: Define data structures and functions
    def get_neighbors(i, j):
        """Returns a list of valid neighbors for a given cell (i, j)."""
        neighbors = []
        if i > 0:
            neighbors.append((i - 1, j))
        if i < n - 1:
            neighbors.append((i + 1, j))
        if j > 0:
            neighbors.append((i, j - 1))
        if j < n - 1:
            neighbors.append((i, j + 1))
        return neighbors

    def dfs(i, j, path, visited):
        """Depth-first search to find all valid k-length paths."""
        visited.add((i, j))
        path.append(grid[i][j])
        if len(path) == k:
            return path
        for ni, nj in get_neighbors(i, j):
            if (ni, nj) not in visited:
                result = dfs(ni, nj, path.copy(), visited.copy())
                if result:
                    return result
        return None

    # Step 3: Explore paths
    min_path = None
    for i in range(n):
        for j in range(n):
            path = dfs(i, j, [], set())
            if path:
                min_path = path
                break
        if min_path:
            break

    # Step 4: Lexicographic comparison
    def compare_paths(path1, path2):
        """Compare two paths lexicographically."""
        for i in range(min(len(path1), len(path2))):
            if path1[i] < path2[i]:
                return True
            elif path1[i] > path2[i]:
                return False
        return len(path1) <= len(path2)

    # Step 5: Finalize output
    return min_path