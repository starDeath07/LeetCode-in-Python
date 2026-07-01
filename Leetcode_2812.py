from typing import List, Deque, Tuple
from collections import deque
import heapq


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n: int = len(grid)
        dirs: List[Tuple[int, int]] = [
            (0, -1),
            (0, 1),
            (1, 0),
            (-1, 0),
        ]

        dist: List[List[int]] = [[-1] * n for _ in range(n)]
        safeness: List[List[int]] = [[-1] * n for _ in range(n)]

        q: Deque[Tuple[int, int]] = deque()

        # Multi-source BFS
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    dist[i][j] = 0

        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        # Max heap (store negative safeness)
        pq: List[Tuple[int, int, int]] = [(-dist[0][0], 0, 0)]
        safeness[0][0] = dist[0][0]

        while pq:
            neg_safe, r, c = heapq.heappop(pq)
            safe: int = -neg_safe

            if r == n - 1 and c == n - 1:
                return safe

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n:
                    new_safe: int = min(safe, dist[nr][nc])

                    if new_safe > safeness[nr][nc]:
                        safeness[nr][nc] = new_safe
                        heapq.heappush(pq, (-new_safe, nr, nc))

        return -1
