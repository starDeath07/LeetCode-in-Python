class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        @cache
        def finder(i: int, j: int, curr: int) -> bool:
            if i >= m or j >= n:
                return False

            sign: str = grid[i][j]
            curr += 1 if sign == "(" else -1

            if i == m - 1 and j == n - 1 and curr == 0:
                return True

            if curr < 0:
                return False

            right: bool = finder(i, j + 1, curr)
            if right:
                return True

            down = finder(i + 1, j, curr)

            if down:
                return True

            return False

        return finder(0, 0, 0)
