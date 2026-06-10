import heapq


class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 0
        obj = SegmentTree(n, nums)
        pq = []

        for i in range(n):
            mini, maxi = obj.query(i, n - 1)
            heapq.heappush(pq, (mini - maxi, i, n - 1))

        while k > 0:
            diff, start, end = heapq.heappop(pq)
            ans += -diff
            mini, maxi = obj.query(start, end - 1)
            heapq.heappush(pq, (mini - maxi, start, end - 1))
            k -= 1

        return ans


class SegmentTree:
    def __init__(self, n: int, arr: list[int]):
        self.n = n
        self.arr = arr
        self.tree = [[0, 0] for _ in range(4 * n)]
        self.build(0, 0, n - 1)

    def build(self, node: int, left: int, right: int):
        if left == right:
            self.tree[node][0] = self.arr[left]
            self.tree[node][1] = self.arr[left]
            return

        mid = left + (right - left) // 2
        self.build(2 * node + 1, left, mid)
        self.build(2 * node + 2, mid + 1, right)
        self.tree[node][0] = min(self.tree[2 * node + 1][0], self.tree[2 * node + 2][0])
        self.tree[node][1] = max(self.tree[2 * node + 1][1], self.tree[2 * node + 2][1])

    def query(self, start: int, end: int) -> list[int]:
        return self._query(0, 0, self.n - 1, start, end)

    def _query(
        self, node: int, left: int, right: int, start: int, end: int
    ) -> list[int]:
        if right < start or end < left:
            return [float("inf"), float("-inf")]

        if start <= left and right <= end:
            return self.tree[node]

        mid = left + (right - left) // 2

        a = self._query(2 * node + 1, left, mid, start, end)
        b = self._query(2 * node + 2, mid + 1, right, start, end)

        return [min(a[0], b[0]), max(a[1], b[1])]
