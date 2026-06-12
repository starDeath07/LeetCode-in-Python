from collections import defaultdict

MOD = 10**9 + 7


class Solution:
    def assignEdgeWeights(
        self, edges: list[list[int]], queries: list[list[int]]
    ) -> list[int]:
        n = len(edges) + 1
        graph: defaultdict[int, list[int]] = defaultdict(list)
        ans: list[int] = []

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        lifting = BinaryLifting(n + 2, graph)

        for u, v in queries:
            lca = lifting.getLCA(u, v)
            steps = lifting.depth[u] + lifting.depth[v] - 2 * lifting.depth[lca]
            ans.append(0 if steps == 0 else pow(2, steps - 1, MOD))

        return ans


class BinaryLifting:
    def __init__(self, n: int, graph: defaultdict[int, list[int]]):
        self.n = n
        self.LOG = self.n.bit_length()
        self.graph = graph
        self.up = [[-1] * self.LOG for _ in range(n + 1)]
        self.depth = [0] * (n + 1)

        self._dfs(1, -1)

    def _dfs(self, node: int, parent: int) -> None:
        self.up[node][0] = parent

        for i in range(1, self.LOG):
            if self.up[node][i - 1] != -1:
                self.up[node][i] = self.up[self.up[node][i - 1]][i - 1]
            else:
                self.up[node][i] = -1

        for nxt in self.graph[node]:
            if nxt != parent:
                self.depth[nxt] = self.depth[node] + 1
                self._dfs(nxt, node)

    def _k_ancestor(self, node: int, k: int) -> int:
        for i in range(self.LOG):
            if node == -1:
                break
            if k & (1 << i):
                node = self.up[node][i]

        return node

    def getLCA(self, u: int, v: int) -> int:
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        diff = self.depth[u] - self.depth[v]
        u = self._k_ancestor(u, diff)

        if u == v:
            return u

        for i in range(self.LOG - 1, -1, -1):
            if self.up[u][i] != self.up[v][i]:
                u = self.up[u][i]
                v = self.up[v][i]

        return self.up[u][0]
