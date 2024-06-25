
def minPath(grid, k):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    min_path = []

    def dfs(i, j, path):
        nonlocal min_path
        visited[i][j] = True
        path.append(grid[i][j])

        if len(path) == k:
            if not min_path or path < min_path:
                min_path = path[:]
        else:
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < n and 0 <= y < n and not visited[x][y]:
                    dfs(x, y, path)

        path.pop()
        visited[i][j] = False

    for i in range(n):
        for j in range(n):
            dfs(i, j, [])

    return min_path