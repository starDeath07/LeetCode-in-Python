class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])

        dp = [[[-1 for _ in range(2)] for _ in range(n)] for _ in range(m)]

        def finder(row: int, col: int, dir: int) -> int:
            if row == m - 1 and col == n - 1:
                return 1

            if row >= m or col >= n:
                return 0

            if dp[row][col][dir] != -1:
                return dp[row][col][dir]

            if grid[row][col] == 1:
                if dir == 0:
                    dp[row][col][dir] = finder(row + 1, col, 1)
                    return dp[row][col][dir]
                else:
                    dp[row][col][dir] = finder(row, col + 1, 0)
                    return dp[row][col][dir]

            dp[row][col][dir] = (
                finder(row, col + 1, 0) % MOD + finder(row + 1, col, 1) % MOD
            )

            return dp[row][col][dir] % MOD

        return finder(0, 0, 0)
