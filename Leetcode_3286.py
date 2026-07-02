from collections import deque


class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        n: int = len(grid)
        m: int = len(grid[0])

        best: list[list[int]] = [[-1] * m for _ in range(n)]

        start_health: int = health - grid[0][0]
        if start_health < 1:
            return False

        q: deque[tuple[int, int, int]] = deque()
        q.append((0, 0, start_health))
        best[0][0] = start_health

        dirs: list[list[int]] = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q:
            r, c, h = q.popleft()

            if r == n - 1 and c == m - 1:
                return True

            for dr, dc in dirs:
                nr: int = r + dr
                nc: int = c + dc

                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue

                new_health: int = h - grid[nr][nc]

                if new_health < 1:
                    continue

                if new_health > best[nr][nc]:
                    best[nr][nc] = new_health
                    q.append((nr, nc, new_health))

        return False
