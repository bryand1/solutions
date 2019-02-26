class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        p = 0
        if not grid:
            return p
        d = ((-1, 0), (0, 1), (1, 0), (0, -1))
        n = len(grid)
        for y in range(n):
            m = len(grid[y])
            for x in range(m):
                if grid[y][x]:
                    for dy, dx in d:
                        i = y + dy
                        j = x + dx
                        if i < 0 or j < 0 or i == n or \
                           j == m or grid[i][j] == 0:
                            p += 1
        return p
