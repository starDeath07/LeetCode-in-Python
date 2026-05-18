from collections import defaultdict, deque
from typing import DefaultDict


class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n: int = len(arr)

        if n == 1:
            return 0

        graph: DefaultDict[int, list[int]] = defaultdict(list)

        for i, num in enumerate(arr):
            graph[num].append(i)

        q: deque[tuple[int, int]] = deque([(0, 0)])

        vis: list[bool] = [False] * n
        vis[0] = True

        while q:
            index, moves = q.popleft()

            if index == n - 1:
                return moves

            # Same value jumps
            if arr[index] in graph:
                for nxt in graph[arr[index]]:
                    if not vis[nxt]:
                        vis[nxt] = True
                        q.append((nxt, moves + 1))

                # Prevent repeated processing
                del graph[arr[index]]

            # index + 1
            if index + 1 < n and not vis[index + 1]:
                vis[index + 1] = True
                q.append((index + 1, moves + 1))

            # index - 1
            if index - 1 >= 0 and not vis[index - 1]:
                vis[index - 1] = True
                q.append((index - 1, moves + 1))

        return -1
