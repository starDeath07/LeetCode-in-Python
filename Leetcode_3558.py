from collections import defaultdict
from typing import DefaultDict


class Solution:
    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        MOD = 10**9 + 7
        graph: DefaultDict[int, list[int]] = defaultdict(list)

        def find_depth(graph: DefaultDict[int, list[int]], node: int, prev: int) -> int:
            max_depth = 0

            for nxt in graph[node]:
                if nxt != prev:
                    max_depth = max(max_depth, find_depth(graph, nxt, node) + 1)
            return max_depth

        def fast_power(base: int, power: int) -> int:
            res = 1
            while power:
                if power & 1 == 1:
                    res = res * base % MOD
                base = base * base % MOD
                power >>= 1
            return res

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        depth = find_depth(graph, 1, 0)
        return fast_power(2, depth - 1)
