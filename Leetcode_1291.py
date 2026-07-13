from collections import deque


class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        dq: deque[int] = deque(range(1, 10))
        ans: list[int] = []

        while dq:
            curr = dq.popleft()
            if low <= curr <= high:
                ans.append(curr)
            next = curr % 10 + 1
            if next <= 9:
                dq.append(curr * 10 + next)

        return ans
