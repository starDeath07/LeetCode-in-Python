from heapq import heappush, heappop


class Solution:
    def minCost(self, n: int, edges: list[list[int]]) -> int:
        inf = 10**10
        costs: list[int] = [inf] * n
        adj: list[list[tuple[int, int]]] = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, 2 * w))

        pq: list[tuple[int, int]] = []
        costs[0] = 0
        heappush(pq, (0, 0))  # cost, node

        while pq:
            cost, node = heappop(pq)

            if node == n - 1:
                return cost

            for next_node, cost_of_next in adj[node]:
                if costs[next_node] > cost + cost_of_next:
                    costs[next_node] = cost + cost_of_next
                    heappush(pq, (costs[next_node], next_node))

        return -1
