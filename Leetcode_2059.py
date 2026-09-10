from collections import deque


class Solution:
    def minimumOperations(self, nums: list[int], start: int, goal: int) -> int:
        q: deque[int] = deque()
        q.append(start)
        seen: list[int] = [-1] * (1001)
        seen[start] = 1
        ans = 0

        while q:
            size = len(q)
            ans += 1

            for _ in range(size):
                curr = q.popleft()
                for num in nums:
                    add = curr + num
                    sub = curr - num
                    xor = curr ^ num

                    if add == goal or sub == goal or xor == goal:
                        return ans

                    if (0 <= add <= 1000) and seen[add] == -1:
                        q.append(add)
                        seen[add] = 1

                    if (0 <= sub <= 1000) and seen[sub] == -1:
                        q.append(sub)
                        seen[sub] = 1

                    if (0 <= xor <= 1000) and seen[xor] == -1:
                        q.append(xor)
                        seen[xor] = 1

        return -1
