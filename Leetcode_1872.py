class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)
        prefix: list[int] = [stones[0]]
        dp: list[int] = [0] * (n + 1)

        for i in range(1, n):
            prefix.append(prefix[-1] + stones[i])

        dp[n - 1] = prefix[-1]

        for index in range(n - 2, 0, -1):
            take = prefix[index] - dp[index + 1]
            skip = dp[index + 1]
            dp[index] = max(take, skip)

        return dp[1]
