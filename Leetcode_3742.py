class Solution:
    def maxPathScore(self, grid: list[list[int]], k: int) -> int:
        NEG_INF = -(10**10)
        n, m = len(grid), len(grid[0])
        dp: list[list[list[int]]] = [
            [[NEG_INF for _ in range(k + 1)] for _ in range(m + 1)]
            for _ in range(n + 1)
        ]

        for i in range(k + 1):
            if grid[n - 1][m - 1] > 0:
                if i > 0:
                    dp[n - 1][m - 1][i] = grid[n - 1][m - 1]
            else:
                dp[n - 1][m - 1][i] = 0

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if i == n - 1 and j == m - 1:
                    continue

                for z in range(k + 1):
                    right: int = 0
                    down: int = 0

                    if grid[i][j] > 0:
                        if z <= 0:
                            dp[i][j][z] = NEG_INF
                            continue

                        right = dp[i][j + 1][z - 1]
                        down = dp[i + 1][j][z - 1]

                        if right != NEG_INF:
                            right += grid[i][j]
                        if down != NEG_INF:
                            down += grid[i][j]
                    else:
                        right = dp[i][j + 1][z]
                        down = dp[i + 1][j][z]

                    dp[i][j][z] = max(right, down)

        return -1 if dp[0][0][k] < 0 else dp[0][0][k]
