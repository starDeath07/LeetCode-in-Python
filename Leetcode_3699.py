class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        gap = r - l + 1
        dp = [1] * gap

        for i in range(2, n + 1):
            tot = 0

            if (i & 1) == 1:
                for j in range(gap):
                    temp = dp[j]
                    dp[j] = tot
                    tot = (tot + temp) % MOD
            else:
                for j in range(gap - 1, -1, -1):
                    temp = dp[j]
                    dp[j] = tot
                    tot = (tot + temp) % MOD

        return (sum(dp) * 2) % MOD
