from __future__ import annotations
from collections import deque


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        q = deque()
        max_sum = -10000000
        level = 0
        ans = 0
        q.append(root)

        while q:
            size = len(q)
            level += 1
            summ = 0
            for _ in range(size):
                curr = q.popleft()
                summ += curr.val

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            if summ > max_sum:
                max_sum = summ
                ans = level

        return ans
