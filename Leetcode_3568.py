from collections import deque


class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        start_r = start_c = -1
        litters: list[tuple[int, int]] = []
        litter_id = [[-1] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                ch = classroom[r][c]
                if ch == "S":
                    start_r, start_c = r, c
                elif ch == "L":
                    litter_id[r][c] = len(litters)
                    litters.append((r, c))

        num_litters = len(litters)
        if num_litters == 0:
            return 0
        target_mask = (1 << num_litters) - 1

        max_energy = [[[-1] * (1 << num_litters) for _ in range(n)] for _ in range(m)]
        max_energy[start_r][start_c][0] = energy

        q = deque([(start_r, start_c, 0, energy)])
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        moves = 0

        while q:
            for _ in range(len(q)):
                r, c, mask, e = q.popleft()

                if mask == target_mask:
                    return moves
                if e == 0:
                    continue

                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if classroom[nr][nc] == "X":
                        continue

                    next_mask = mask
                    if classroom[nr][nc] == "L":
                        next_mask |= 1 << litter_id[nr][nc]

                    next_energy = energy if classroom[nr][nc] == "R" else e - 1

                    if next_energy > max_energy[nr][nc][next_mask]:
                        max_energy[nr][nc][next_mask] = next_energy
                        q.append((nr, nc, next_mask, next_energy))

            moves += 1

        return -1
