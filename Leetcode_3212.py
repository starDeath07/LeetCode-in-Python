class Solution:
    class Point:
        def __init__(self):
            self.x = 0
            self.y = 0

    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])

        point = [[self.Point() for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                up = point[i - 1][j] if i > 0 else self.Point()
                left = point[i][j - 1] if j > 0 else self.Point()
                sub = point[i - 1][j - 1] if i > 0 and j > 0 else self.Point()

                addX = 1 if grid[i][j] == "X" else 0
                addY = 1 if grid[i][j] == "Y" else 0

                point[i][j].x = up.x + left.x - sub.x + addX
                point[i][j].y = up.y + left.y - sub.y + addY

                if point[i][j].x > 0 and point[i][j].x == point[i][j].y:
                    ans += 1

        return ans


# Another better Solution


class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        ans, m, n = 0, len(grid), len(grid[0])
        up: list[list[int]] = [[0, 0] for _ in range(n)]

        for i in range(m):
            curr = [0, 0]
            for j in range(n):
                up[j][0] += 1 if grid[i][j] == "X" else 0
                up[j][1] += 1 if grid[i][j] == "Y" else 0

                curr[0] += up[j][0]
                curr[1] += up[j][1]

                if curr[0] > 0 and curr[0] == curr[1]:
                    ans += 1
        return ans
