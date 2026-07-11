class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        ans = 0

        self.parent: list[int] = []
        self.edge_count: list[int] = []
        self.node_count: list[int] = []

        for i in range(n):
            self.parent.append(i)
            self.node_count.append(1)
            self.edge_count.append(0)

        for u, v in edges:
            self.union(u, v)

        for i in range(n):
            if self.parent[i] == i:
                node = self.parent[i]
                count = self.node_count[node]
                expected_count = count * (count - 1) // 2
                if expected_count == self.edge_count[node]:
                    ans += 1
        return ans

    def find_parent(self, u: int) -> int:
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find_parent(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int) -> None:
        pu = self.find_parent(u)
        pv = self.find_parent(v)

        if pu == pv:
            self.edge_count[pu] += 1

        else:
            self.parent[pv] = pu
            self.edge_count[pu] += self.edge_count[pv] + 1
            self.node_count[pu] += self.node_count[pv]
