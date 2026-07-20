class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m = len(grid)
        n = len(grid[0])
        ans: list[list[int]] = [[0] * n for _ in range(m)]

        size = m * n
        k %= size

        for i in range(m):
            for j in range(n):
                index = i * n + j
                new_index = (index + k) % size
                new_i = new_index // n
                new_j = new_index % n
                ans[new_i][new_j] = grid[i][j]

        return ans
