from typing import List


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        size = min(m, n)
        # Create prefix 2D arrays for calculating the sum of rows and cols
        pref_row: List[List[int]] = [[0] * (n + 1) for _ in range(m)]
        pref_col: List[List[int]] = [[0] * n for _ in range(m + 1)]

        # Populate the prefix arrays
        for r in range(m):
            for c in range(n):
                pref_row[r][c + 1] = pref_row[r][c] + grid[r][c]
                pref_col[r + 1][c] = pref_col[r][c] + grid[r][c]

        for k in range(size, 0, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if self.valid(r, c, k, grid, pref_row, pref_col):
                        return k
        return 1

    def valid(
        self,
        r: int,
        c: int,
        size: int,
        grid: List[List[int]],
        pref_row: List[List[int]],
        pref_col: List[List[int]],
    ) -> bool:
        target = pref_row[r][c + size] - pref_row[r][c]
        d1 = d2 = 0
        # Check for row sum if equal to target
        for i in range(size):
            curr = pref_row[r + i][c + size] - pref_row[r + i][c]
            if curr != target:
                return False
        # Check for col sum equal to target
        for i in range(size):
            curr = pref_col[r + size][c + i] - pref_col[r][c + i]
            if curr != target:
                return False
        # Check for diagonal sum equal to target and equal in sum
        for i in range(size):
            d1 += grid[r + i][c + i]
            d2 += grid[r + i][c + size - 1 - i]

        if d1 != d2 or d1 != target:
            return False

        return True
