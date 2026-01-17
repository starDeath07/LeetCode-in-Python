from typing import List


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_side = 0

        for i in range(n):
            for j in range(i + 1, n):
                min_x = max(bottomLeft[i][0], bottomLeft[j][0])  # find the min of X for the intersecting rectangle
                max_x = min(topRight[i][0], topRight[j][0])  # find the max of X for the intersecting rectangle
                min_y = max(bottomLeft[i][1], bottomLeft[j][1])  # find the min of Y for the intersecting rectangle
                max_y = min(topRight[i][1], topRight[j][1])  # find the max of Y for the intersecting rectangle

                side = min(max_x - min_x, max_y - min_y)  # find the min size to form square
                max_side = max(max_side, side)  # find the max side to form the largest square

        return max_side * max_side
