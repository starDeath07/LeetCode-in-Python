class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # dp[i][j] = [min_product, max_product]
        dp: list[list[list[int]]] = [
            [[10**10, -(10**10)] for _ in range(n)] for _ in range(m)
        ]

        dp[m - 1][n - 1] = [grid[m - 1][n - 1], grid[m - 1][n - 1]]

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row == m - 1 and col == n - 1:
                    continue

                min_val = 10**10
                max_val = -(10**10)
                curr = grid[row][col]

                if row + 1 < m:
                    a, b = curr * dp[row + 1][col][0], curr * dp[row + 1][col][1]
                    min_val = min(min_val, a, b)
                    max_val = max(max_val, a, b)

                if col + 1 < n:
                    a, b = curr * dp[row][col + 1][0], curr * dp[row][col + 1][1]
                    min_val = min(min_val, a, b)
                    max_val = max(max_val, a, b)

                dp[row][col] = [min_val, max_val]

        MOD = 10**9 + 7
        return -1 if dp[0][0][1] < 0 else dp[0][0][1] % MOD
