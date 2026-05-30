from bisect import bisect_left, bisect_right, insort


class SegmentTree:
    def __init__(self, n: int) -> None:
        self.n: int = n
        self.tree: list[int] = [0] * (4 * n)

    def update(self, index: int, value: int) -> None:
        self._update(0, 0, self.n - 1, index, value)

    def query(self, left: int, right: int) -> int:
        if left > right:
            return 0
        return self._query(0, 0, self.n - 1, left, right)

    def _update(self, node: int, start: int, end: int, index: int, value: int) -> None:
        if start == end:
            self.tree[node] = value
            return

        mid = start + (end - start) // 2

        if index <= mid:
            self._update(2 * node + 1, start, mid, index, value)
        else:
            self._update(2 * node + 2, mid + 1, end, index, value)

        self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def _query(self, node: int, start: int, end: int, left: int, right: int) -> int:
        if start > right or end < left:
            return 0

        if start >= left and end <= right:
            return self.tree[node]

        mid = start + (end - start) // 2

        l: int = self._query(2 * node + 1, start, mid, left, right)
        r: int = self._query(2 * node + 2, mid + 1, end, left, right)

        return max(l, r)


class Solution:
    def getResults(self, queries: list[list[int]]) -> list[bool]:
        max_val: int = 0
        ans: list[bool] = []

        for q in queries:
            max_val = max(max_val, q[1])

        limit: int = max_val + 1

        arr: list[int] = [0, limit]

        tree = SegmentTree(limit + 1)
        tree.update(limit, limit)

        for q in queries:
            type_: int = q[0]
            x: int = q[1]

            if type_ == 1:
                pos: int = bisect_left(arr, x)

                if pos < len(arr) and arr[pos] == x:
                    continue

                prev: int = arr[pos - 1]
                next_: int = arr[pos]

                tree.update(x, x - prev)
                tree.update(next_, next_ - x)

                insort(arr, x)

            else:
                prev: int = arr[bisect_right(arr, x) - 1]

                gap: int = tree.query(0, prev)
                maxGap: int = max(gap, x - prev)

                ans.append(q[2] <= maxGap)

        return ans
