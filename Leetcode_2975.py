from typing import List, Set


class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        # Add the boundaries
        hFences.append(1)
        hFences.append(m)
        MOD = 10**9 + 7
        # Add the boundaries
        vFences.append(1)
        vFences.append(n)

        found: Set[int] = set()

        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                found.add(abs(hFences[i] - hFences[j]))

        max_side = -1
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                side = abs(vFences[i] - vFences[j])
                if side in found:
                    max_side = max(max_side, side)

        return -1 if max_side == -1 else (max_side * max_side) % MOD
