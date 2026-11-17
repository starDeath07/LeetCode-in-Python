class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = 10**18

        partition_dp: list[list[int]] = [[INF] * (k + 1) for _ in range(n + 1)]
        cost_dp: list[list[int]] = [[-1] * (n + 1) for _ in range(n + 1)]

        partition_dp[n][0] = 0

        def get_cost(i: int, j: int) -> int:
            length = j - i + 1
            min_cost = INF

            if cost_dp[i][j] != -1:
                return cost_dp[i][j]

            for d in range(1, length):
                if length % d != 0:
                    continue

                cost = 0

                for group in range(0, d):
                    left = i + group
                    right = left + (length // d - 1) * d

                    while left < right:
                        if s[left] != s[right]:
                            cost += 1
                        left += d
                        right -= d

                min_cost = min(min_cost, cost)

            cost_dp[i][j] = min_cost
            return min_cost

        for i in range(n):
            for j in range(i + 1, n):
                cost_dp[i][j] = get_cost(i, j)

        for start in range(n - 1, -1, -1):
            for part in range(1, k + 1):
                if start + 2 * part > n:
                    continue
                ans = INF

                for i in range(start + 1, n):
                    remaining_cost = partition_dp[i + 1][part - 1]
                    if remaining_cost == INF:
                        continue
                    ans = min(ans, remaining_cost + cost_dp[start][i])

                partition_dp[start][part] = ans

        return partition_dp[0][k]
