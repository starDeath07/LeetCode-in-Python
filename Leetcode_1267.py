class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0

        row: list[int] = [0] * m
        col: list[int] = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
                    ans += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and row[i] == 1 and col[j] == 1:
                    ans -= 1

        return ans
