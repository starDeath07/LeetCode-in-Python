class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp: list[int] = [0] * (n + 1)
        last_seen: list[int] = [0] * 26

        dp[0] = 1

        for i in range(1, n + 1):
            index = ord(s[i - 1]) - ord("a")
            dp[i] = (dp[i - 1] * 2) % MOD

            if last_seen[index]:
                dp[i] = (dp[i] - last_seen[index] + MOD) % MOD

            last_seen[index] = dp[i - 1]

        return (dp[n] + MOD - 1) % MOD
