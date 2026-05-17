from collections import deque


class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        n = len(arr)
        q: deque[int] = deque()
        vis = [False] * n

        q.append(start)
        vis[start] = True
        while q:
            current = q.popleft()

            if arr[current] == 0:
                return True
            forward = current + arr[current]
            backward = current - arr[current]

            if forward < n and not vis[forward]:
                q.append(forward)
                vis[forward] = True

            if backward >= 0 and not vis[backward]:
                q.append(backward)
                vis[backward] = True

        return False
