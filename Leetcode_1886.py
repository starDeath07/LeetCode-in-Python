class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        for _ in range(4):
            if self.valid(mat, target):
                return True
            mat = self.rotate(mat)

        return False

    def valid(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        for i in range(len(mat)):
            if mat[i] != target[i]:
                return False
        return True

    def rotate(self, mat: list[list[int]]) -> list[list[int]]:
        n = len(mat)
        rotated = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                rotated[j][n - i - 1] = mat[i][j]
        return rotated
