class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: list[str],
        changed: list[str],
        cost: list[int],
    ) -> int:
        n = len(source)
        string_to_index: dict[str, int] = {}
        size_of_original: set[int] = set()
        index: int = 0
        # create indexing to make graph easy so we can take each node as integer instead of string
        for i in range(len(original)):
            size_of_original.add(len(original[i]))
            if original[i] not in string_to_index:
                string_to_index[original[i]] = index
                index += 1

            if changed[i] not in string_to_index:
                string_to_index[changed[i]] = index
                index += 1

        INF: int = 10**15
        distance: list[list[int]] = [[INF] * index for _ in range(index)]
        dp: list[int] = [INF] * (n + 1)

        # fill the distance array which are possible to reach
        for i in range(len(original)):
            u, v, w = string_to_index[original[i]], string_to_index[changed[i]], cost[i]
            distance[u][v] = min(distance[u][v], w)

        # find all the distances using Floyd Warshall Algo
        for k in range(index):
            for i in range(index):
                for j in range(index):
                    if distance[i][k] < INF and distance[k][j] < INF:
                        distance[i][j] = min(
                            distance[i][j], distance[i][k] + distance[k][j]
                        )

        dp[0] = 0

        for i in range(n):
            if dp[i] == INF:
                continue

            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])

            for sizes in size_of_original:
                if sizes + i > n:
                    continue

                u = string_to_index.get(source[i : i + sizes], -1)
                v = string_to_index.get(target[i : i + sizes], -1)

                if u == -1 or v == -1:
                    continue

                if distance[u][v] < INF:
                    dp[i + sizes] = min(dp[i + sizes], dp[i] + distance[u][v])

        return -1 if dp[n] == INF else dp[n]
