class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        ans = 0

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j]:
                    ans = max(ans, self.finder(grid, i, j))

        return ans

    def finder(self, grid: list[list[int]], row: int, col: int) -> int:
        if row < 0 or row >= self.m or col < 0 or col >= self.n or grid[row][col] == 0:
            return 0

        curr = grid[row][col]
        grid[row][col] = 0

        curr += self.finder(grid, row, col + 1)
        curr += self.finder(grid, row, col - 1)
        curr += self.finder(grid, row + 1, col)
        curr += self.finder(grid, row - 1, col)

        return curr
