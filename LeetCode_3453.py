from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        half_area = 0.0
        start = float("inf")
        end = 0.0

        for point in squares:
            start = min(start, point[1])
            end = max(end, point[1] + point[2])
            half_area += point[2] * point[2]

        half_area /= 2.0
        precise = float(1e-5)

        while end - start > precise:
            mid = start + (end - start) / 2
            bottom_area = self.finder(squares, mid)
            if bottom_area >= half_area:
                end = mid
            else:
                start = mid
        return (start + end) / 2

    def finder(self, squares: List[List[int]], line: float) -> float:
        area = 0.0

        for point in squares:
            y = point[1]
            l = point[2]

            height = min(max(line - y, 0), l)
            area += l * height

        return area
