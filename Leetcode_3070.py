class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        ans, m, n = 0, len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                up = grid[i - 1][j] if i > 0 else 0
                left = grid[i][j - 1] if j > 0 else 0
                sub = grid[i - 1][j - 1] if i > 0 and j > 0 else 0
                grid[i][j] += up + left - sub
                if grid[i][j] <= k:
                    ans += 1
        return ans
