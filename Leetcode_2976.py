class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: list[str],
        changed: list[str],
        cost: list[int],
    ) -> int:
        ans = 0
        n, m = len(source), len(target)

        if n != m:
            return -1
        inf = 10**10
        dp: list[list[int]] = [[inf] * 26 for _ in range(26)]

        # map cost from converting u to v and update it

        for i in range(len(original)):
            u, v, w = ord(original[i]) - 97, ord(changed[i]) - 97, cost[i]
            dp[u][v] = min(dp[u][v], w)

        # Use Floyd Warshall Algorithm to calculate the minimum cost for each possible conversion
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

        ans = 0
        for i in range(n):
            u, v = ord(source[i]) - 97, ord(target[i]) - 97
            if u == v:
                continue
            if dp[u][v] == inf:
                return -1
            ans += dp[u][v]

        return ans
