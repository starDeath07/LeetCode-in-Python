# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        ans: list[int] = [-1, -1]

        index1 = -1
        index2 = -1
        pos = 0

        curr = head

        first: int = curr.val
        second: int = curr.next.val

        curr = curr.next.next

        def is_critical(a: int, b: int, c: int) -> bool:
            return a < b > c or a > b < c

        while curr != None:
            if is_critical(first, second, curr.val):
                if index1 == -1:
                    index1 = pos
                    first = second
                    second = curr.val
                    curr = curr.next
                    pos += 1
                    continue
                elif index2 == -1:
                    ans[0] = pos - index1
                ans[0] = min(ans[0], pos - index2)
                index2 = pos
            first = second
            second = curr.val
            curr = curr.next
            pos += 1

        if index1 != -1 and index2 != -1:
            ans[1] = index2 - index1
        return ans
