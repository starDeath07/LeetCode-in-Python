class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        n = len(boxGrid)
        m = len(boxGrid[0])

        ans = [[""] * n for _ in range(m)]

        for i in range(n):
            empty = m - 1

            for j in range(m - 1, -1, -1):
                if boxGrid[i][j] == "*":
                    ans[j][n - 1 - i] = "*"
                    empty = j - 1

                elif boxGrid[i][j] == "#":
                    ans[empty][n - 1 - i] = "#"
                    if empty != j:
                        ans[j][n - 1 - i] = "."
                    empty -= 1

                else:  # '.'
                    ans[j][n - 1 - i] = "."

        return ans
