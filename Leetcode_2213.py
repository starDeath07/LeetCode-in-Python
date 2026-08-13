from typing import List, Optional


class Solution:
    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: List[int]
    ) -> List[int]:
        arr: List[str] = list(s)
        n: int = len(arr)
        m: int = len(queryIndices)

        sg: SegmentTree = SegmentTree(n, arr)
        ans: List[int] = [0] * m

        for i in range(m):
            sg.update(0, 0, n - 1, queryIndices[i], queryCharacters[i])
            ans[i] = sg.tree[0].best

        return ans


class Node:
    def __init__(
        self, length: int, prefix: int, suffix: int, best: int, left: str, right: str
    ) -> None:
        self.length: int = length
        self.prefix: int = prefix
        self.suffix: int = suffix
        self.best: int = best
        self.left: str = left
        self.right: str = right


class SegmentTree:
    def __init__(self, n: int, arr: List[str]) -> None:
        self.arr: List[str] = arr
        self.tree: List[Optional[Node]] = [None] * (4 * n)

        self.build(0, 0, n - 1, arr)

    def build(self, index: int, start: int, end: int, arr: List[str]) -> None:
        if start == end:
            self.tree[index] = Node(1, 1, 1, 1, arr[start], arr[start])
            return

        mid: int = start + (end - start) // 2

        self.build(2 * index + 1, start, mid, arr)

        self.build(2 * index + 2, mid + 1, end, arr)

        self.tree[index] = self.merge(
            self.tree[2 * index + 1], self.tree[2 * index + 2]
        )

    def merge(self, a: Optional[Node], b: Optional[Node]) -> Optional[Node]:
        if a is None:
            return b

        if b is None:
            return a

        res: Node = Node(
            a.length + b.length,
            a.prefix,
            b.suffix,
            max(a.best, b.best),
            a.left,
            b.right,
        )

        if a.right == b.left:
            res.best = max(res.best, a.suffix + b.prefix)

            if a.prefix == a.length:
                res.prefix = a.length + b.prefix

            if b.suffix == b.length:
                res.suffix = b.length + a.suffix

        return res

    def update(self, index: int, start: int, end: int, pos: int, c: str) -> None:
        if start == end:
            self.arr[pos] = c

            self.tree[index] = Node(1, 1, 1, 1, c, c)
            return

        mid: int = start + (end - start) // 2

        if pos <= mid:
            self.update(2 * index + 1, start, mid, pos, c)
        else:
            self.update(2 * index + 2, mid + 1, end, pos, c)

        self.tree[index] = self.merge(
            self.tree[2 * index + 1], self.tree[2 * index + 2]
        )
