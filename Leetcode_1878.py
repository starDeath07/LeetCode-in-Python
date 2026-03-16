from sortedcontainers import SortedSet


class Solution:
    def getBiggestThree(self, grid: list[list[int]]) -> list[int]:
        m: int = len(grid)
        n: int = len(grid[0])
        ans: SortedSet[int] = SortedSet()

        def valid(row: int, col: int, side: int) -> bool:
            if row - side < 0:
                return False
            if row + side >= m:
                return False
            if col - side < 0:
                return False
            if col + side >= n:
                return False
            return True

        for row in range(m):
            for col in range(n):
                ans.add(grid[row][col])
                side = 1

                while True:
                    if not valid(row, col, side):
                        break
                    sum = 0
                    for k in range(side):
                        sum += grid[row - side + k][col + k]
                        sum += grid[row + k][col + side - k]
                        sum += grid[row + side - k][col - k]
                        sum += grid[row - k][col - side + k]
                    ans.add(sum)
                    side += 1

                    if len(ans) > 3:
                        ans.pop(0)

        res: list[int] = []
        while ans:
            res.append(ans.pop())
        return res
