class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[[-1] * 1024 for _ in range(m)] for _ in range(n)]

        def finder(x: int, y: int, curr: int) -> int:
            if x >= n or y >= m:
                return 10**10

            curr ^= grid[x][y]

            if dp[x][y][curr] != -1:
                return dp[x][y][curr]

            if x == n - 1 and y == m - 1:
                return curr

            right = finder(x + 1, y, curr)
            left = finder(x, y + 1, curr)

            dp[x][y][curr] = min(right, left)
            return dp[x][y][curr]

        return finder(0, 0, 0)
