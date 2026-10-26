class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0

        def finder(row: int, col: int) -> int:
            if row < 0 or row >= n or col < 0 or col >= m or grid[row][col] < 1:
                return 0

            total = grid[row][col]
            grid[row][col] = -1

            total += finder(row + 1, col)
            total += finder(row, col + 1)
            total += finder(row - 1, col)
            total += finder(row, col - 1)

            return total

        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    curr = finder(i, j)
                    if curr % k == 0:
                        ans += 1

        return ans
