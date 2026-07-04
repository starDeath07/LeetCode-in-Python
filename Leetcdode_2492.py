class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> None:
            pa, pb = find(a), find(b)

            if pa == pb:
                return

            if rank[pa] < rank[pb]:
                parent[pa] = pb
            elif rank[pa] > rank[pb]:
                parent[pb] = pa
            else:
                parent[pb] = pa
                rank[pa] += 1

        for u, v, _ in roads:
            union(u, v)

        root = find(1)
        ans = 10**10

        for u, v, d in roads:
            if find(u) == root:
                ans = min(ans, d)

        return ans
