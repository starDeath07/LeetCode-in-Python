class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        dp: list[int] = [0, 0]
        ans = 0
        total = 0

        for num in arr:
            total = (total + num) % 2
            if total == 0:
                ans += dp[1]
            else:
                ans += 1
                ans += dp[0]
            dp[total] += 1
            ans %= MOD

        return ans
