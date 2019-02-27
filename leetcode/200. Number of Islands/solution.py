# 200. Number of Islands
from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands = 0
        self.visited = set()
        self.length = len(grid)
        self.width = len(grid[0])
        for y in range(self.length):
            for x in range(self.width):
                if grid[y][x] == "1" and ((y, x) not in self.visited):
                    self.bfs(grid, y, x)
                    islands += 1
        return islands

    def bfs(self, grid, y, x):
        frontier = deque()
        frontier.appendleft((y, x))
        self.visited.add((y, x))
        while frontier:
            curr = frontier.pop()
            for i, j in self.neighbors(grid, *curr):
                if grid[i][j] == "1" and ((i, j) not in self.visited):
                    self.visited.add((i, j))
                    frontier.appendleft((i, j))

    def neighbors(self, grid, y, x): 
        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            i = y + dy
            j = x + dx
            if i >= 0 and j >= 0 and i < self.length and j < self.width:
                yield i, j

if __name__ == '__main__':
    ex1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]
    solution = Solution()
    print(solution.numIslands(ex1))
