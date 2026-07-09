class Solution:
    def pathExistenceQueries(
        self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]
    ) -> list[bool]:
        ob = DSU(n)
        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                ob.union(i - 1, i)

        ans: list[bool] = []

        for u, v in queries:
            ans.append(ob.find_parent(u) == ob.find_parent(v))

        return ans


class DSU:
    def __init__(self, n: int):
        self.n = n
        self.parent = [i for i in range(n)]

    def find_parent(self, u: int):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find_parent(self.parent[u])

        return self.parent[u]

    def union(self, u: int, v: int):
        pu = self.find_parent(u)
        pv = self.find_parent(v)

        if pu == pv:
            return

        self.parent[pv] = pu
