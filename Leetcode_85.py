from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]):
        n = len(matrix[0])
        ans = 0

        def finder(compressed: List[int]):
            stack: List[tuple[int, int]] = []
            best = 0
            for i, h in enumerate(compressed):
                start = i
                while stack and stack[-1][1] > h:
                    index, height = stack.pop()
                    best = max(best, (i - index) * height)
                    start = index

                stack.append((start, h))

            while stack:
                index, height = stack.pop()
                best = max(best, (n - index) * height)

            return best

        compressed: List[int] = [0] * n

        for mat in matrix:
            for i in range(n):
                if mat[i] != "0":
                    compressed[i] += 1
                else:
                    compressed[i] = 0
            ans = max(ans, finder(compressed))
        return ans
