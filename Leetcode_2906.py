class Solution:
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        ans: list[list[int]] = [[0] * n for _ in range(m)]
        MOD = 12345
        mult = 1
        for i in range(m):
            for j in range(n):
                ans[i][j] = mult
                mult = (mult * grid[i][j]) % MOD

        mult = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                ans[i][j] = (ans[i][j] * mult) % MOD
                mult = (mult * grid[i][j]) % MOD

        return ans
