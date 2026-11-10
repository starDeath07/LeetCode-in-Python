class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        dp: list[int] = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = 10**10
            c1: int = 10**10
            c2: int = 10**10
            c3: int = 10**10

            if i + 1 <= n:
                c1 = costs[i] + 1 + dp[i + 1]
            if i + 2 <= n:
                c2 = costs[i + 1] + 4 + dp[i + 2]
            if i + 3 <= n:
                c3 = costs[i + 2] + 9 + dp[i + 3]

            dp[i] = min(c1, c2, c3)

        return dp[0]
