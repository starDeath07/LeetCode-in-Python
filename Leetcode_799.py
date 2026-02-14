class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [0.0] * (query_row + 1)
        dp[0] = poured

        for i in range(query_row):
            for j in range(i, -1, -1):  # iterate right to left
                extra = max(0.0, (dp[j] - 1) / 2.0)
                dp[j] = extra
                dp[j + 1] += extra

        return min(1.0, dp[query_glass])
