from typing import List
from collections import deque


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        layers = min(m, n) // 2

        for layer in range(layers):
            top = left = layer
            bottom = m - 1 - layer
            right = n - 1 - layer

            dq: deque[int] = deque()

            # extract
            for i in range(left, right):
                dq.append(grid[top][i])

            for i in range(top, bottom):
                dq.append(grid[i][right])

            for i in range(right, left, -1):
                dq.append(grid[bottom][i])

            for i in range(bottom, top, -1):
                dq.append(grid[i][left])

            dq.rotate(-(k % len(dq)))

            # write back
            for i in range(left, right):
                grid[top][i] = dq.popleft()

            for i in range(top, bottom):
                grid[i][right] = dq.popleft()

            for i in range(right, left, -1):
                grid[bottom][i] = dq.popleft()

            for i in range(bottom, top, -1):
                grid[i][left] = dq.popleft()

        return grid
