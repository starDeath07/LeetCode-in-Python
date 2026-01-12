from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n: int = len(points)
        ans: int = 0

        for i in range(1, n):
            dx: int = abs(points[i][0] - points[i - 1][0])
            dy: int = abs(points[i][1] - points[i - 1][1])
            ans += min(dy, dx) + abs(dy - dx)
        return ans
