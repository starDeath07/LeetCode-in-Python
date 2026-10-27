class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ans: list[list[str]] = [["#"] * n for _ in range(m)]

        for col in range(n):
            ans[0][col] = "."

        for row in range(m):
            ans[row][n - 1] = "."

        res: list[str] = []

        for row in ans:
            res.append("".join(row))

        return res
