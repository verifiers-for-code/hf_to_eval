def minPath(grid, k):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    min_path = []

    def dfs(x, y, path):
        if len(path) == k:
            if not min_path or path < min_path:
                min_path[:] = path
            return

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, path + [grid[nx][ny]])
                visited[nx][ny] = False

    for i in range(n):
        for j in range(n):
            dfs(i, j, [grid[i][j]])

    return min_path