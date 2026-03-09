class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        dp = [[[0] * 2 for _ in range(one + 1)] for _ in range(zero + 1)]
        dp[0][0][0] = dp[0][0][1] = 1
        MOD = 10**9 + 7

        for z in range(zero + 1):
            for o in range(one + 1):
                # check for zeros
                for i in range(1, min(limit, z) + 1):
                    dp[z][o][0] = (dp[z][o][0] + dp[z - i][o][1]) % MOD

                # check for ones
                for i in range(1, min(limit, o) + 1):
                    dp[z][o][1] = (dp[z][o][1] + dp[z][o - i][0]) % MOD

        return (dp[zero][one][0] + dp[zero][one][1]) % MOD
