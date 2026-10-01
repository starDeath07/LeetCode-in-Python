from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        deq: deque[str] = deque()

        for c in s:
            if c in "([{":
                deq.append(c)
            elif len(deq) == 0:
                return False
            elif c == ")" and deq[-1] != "(":
                return False
            elif c == "}" and deq[-1] != "{":
                return False
            elif c == "]" and deq[-1] != "[":
                return False
            else:
                deq.pop()

        return len(deq) == 0
